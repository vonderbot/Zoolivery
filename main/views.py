from itertools import chain
from operator import attrgetter
from django.shortcuts import render, redirect
from .models import product, user, role, receipt_status, \
    delivery_type, receipt, receipt_has_product, product_type
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ValidationError
from django.http import JsonResponse


def change_status(request, new_status_id, receipt_id):
    receipt_to_change = receipt.objects.get(id=int(receipt_id))
    status_to_change = receipt_status.objects.get(id=int(new_status_id))
    receipt_to_change.status_id = status_to_change
    receipt_to_change.save()
    return JsonResponse({'new_status_id': new_status_id, 'receipt_id': receipt_id})


def all_receipt_list(request):
    header_secret_number = 5
    if request.method == 'POST':
        # my_receipts = receipt.objects.filter(id=request.POST["number"])
        lname = request.POST["number"]
        my_receipts = receipt.objects.raw('SELECT * FROM main_receipt WHERE id = %s', [lname])
    else:
        # my_receipts = receipt.objects.all()
        my_receipts = receipt.objects.raw('SELECT * FROM main_receipt')
    # all_receipt_has_product = receipt_has_product.objects.all()
    all_receipt_has_product = receipt_has_product.objects.raw('SELECT * FROM main_receipt_has_product')
    # all_receipts_statuses = receipt_status.objects.all()
    all_receipts_statuses = receipt_status.objects.raw('SELECT * FROM main_receipt_status')
    return render(request, 'main/all_receipt_list.html', {"header_secret_number": header_secret_number,
                                                          "username_login": request.session['user_login'],
                                                          "my_receipts": my_receipts,
                                                          'all_receipts_statuses': all_receipts_statuses,
                                                          'all_receipt_has_product': all_receipt_has_product})


def my_receipt_list(request):
    header_secret_number = 5
    user_data = user.objects.get(login=request.session['user_login'])
    if request.method == 'POST':
        my_receipts = receipt.objects.filter(user_id=user_data, id=request.POST["number"])
    else:
        my_receipts = receipt.objects.filter(user_id=user_data)
        # lname = user_data
        # my_receipts = receipt.objects.raw('SELECT * FROM main_receipt WHERE user_id = %s', [lname])
    return render(request, 'main/my_receipt_list.html', {"header_secret_number": header_secret_number,
                                                         "username_login": request.session['user_login'],
                                                         "my_receipts": my_receipts})


@csrf_exempt
def receipt_check(request):
    if request.method == 'POST':
        try:
            # products = product.objects.all()
            products = product.objects.raw('SELECT * FROM main_product')
            for element2 in products:
                amount = 0
                for element in request.session['cart']:
                    if element == str(element2.id):
                        amount += 1
                if amount > 0 and amount > element2.amount:
                    raise ValidationError("error")
            new_receipt = receipt()
            if request.POST["post_station_address"] != "":
                contact_user = request.POST["phone"]
                address = request.POST["post_station_address"]
                products_in_cart = []
                sum_cost = 0
                # products = product.objects.all()
                products = product.objects.raw('SELECT * FROM main_product')
                for element in request.session['cart']:
                    for element2 in products:
                        if element == str(element2.id):
                            products_in_cart.append(element2)
                            break
                for element in products_in_cart:
                    sum_cost += element.price
                status_id = receipt_status.objects.get(name="Новый")
                delivery_id = delivery_type.objects.get(name="Почта")
                if request.session['user_login'] != "":
                    user_id = user.objects.get(login=request.session['user_login'])
                    new_receipt = receipt(contact=contact_user, address=address,
                                          sum_cost=sum_cost, status_id=status_id,
                                          delivery_id=delivery_id, user_id=user_id)
                else:
                    new_receipt = receipt(contact=contact_user, address=address,
                                          sum_cost=sum_cost, status_id=status_id,
                                          delivery_id=delivery_id)
                new_receipt.save()
                message = "Заказ почтой оформлен!"
            elif request.POST["address"] != "":
                contact_user = request.POST["phone"]
                address = request.POST["address"]
                products_in_cart = []
                sum_cost = 0
                # products = product.objects.all()
                products = product.objects.raw('SELECT * FROM main_product')
                for element in request.session['cart']:
                    for element2 in products:
                        if element == str(element2.id):
                            products_in_cart.append(element2)
                            break
                for element in products_in_cart:
                    sum_cost += element.price
                status_id = receipt_status.objects.get(name="Новый")
                delivery_id = delivery_type.objects.get(name="Курьер")
                if request.session['user_login'] != "":
                    user_id = user.objects.get(login=request.session['user_login'])
                    new_receipt = receipt(contact=contact_user, address=address,
                                          sum_cost=sum_cost, status_id=status_id,
                                          delivery_id=delivery_id, user_id=user_id)
                else:
                    new_receipt = receipt(contact=contact_user, address=address,
                                          sum_cost=sum_cost, status_id=status_id,
                                          delivery_id=delivery_id)
                new_receipt.save()
                message = "Заказ курьером оформлен!"
            else:
                contact_user = request.POST["phone"]
                products_in_cart = []
                sum_cost = 0
                # products = product.objects.all()
                products = product.objects.raw('SELECT * FROM main_product')
                for element in request.session['cart']:
                    for element2 in products:
                        if element == str(element2.id):
                            products_in_cart.append(element2)
                            break
                for element in products_in_cart:
                    sum_cost += element.price
                status_id = receipt_status.objects.get(name="Новый")
                delivery_id = delivery_type.objects.get(name="Самовывоз")
                if request.session['user_login'] != "":
                    user_id = user.objects.get(login=request.session['user_login'])
                    new_receipt = receipt(contact=contact_user,
                                          sum_cost=sum_cost, status_id=status_id,
                                          delivery_id=delivery_id, user_id=user_id)
                else:
                    new_receipt = receipt(contact=contact_user,
                                          sum_cost=sum_cost, status_id=status_id,
                                          delivery_id=delivery_id)
                new_receipt.save()
                message = "Заказ самовывозом оформлен!"
            receipt_id = new_receipt
            # products = product.objects.all()
            products = product.objects.raw('SELECT * FROM main_product')
            for element2 in products:
                product_id = element2
                amount = 0
                for element in request.session['cart']:
                    if element == str(element2.id):
                        amount += 1
                if amount > 0:
                    element2.amount -= amount
                    element2.save()
                    price = amount * element2.price
                    new_receipt_has_product = receipt_has_product(receipt_id=receipt_id, product_id=product_id,
                                                                  price=price, amount=amount)
                    new_receipt_has_product.save()
        except ValidationError as e:
            message = "Вы пытаетесь купить больше товара, чем есть на складе. Заказ не был отправлен, повторите попытку."
        request.session['cart'] = []
        return render(request, 'main/solo_message.html', {"message": message,
                                                          "username_login": request.session['user_login']})
    else:
        message = "Ошибка,был отправлен GET запрос!"
        return render(request, 'main/solo_message.html', {"message": message,
                                                          "username_login": request.session['user_login']})


def backet_data_save(request, change):
    if 'cart' not in request.session:
        request.session['cart'] = []
    request.session['cart'].append(change)
    request.session.modified = True
    return JsonResponse({'foo': change})


def registratiohn_ceck(request):
    if request.method == 'POST':
        if request.POST["password1"] == request.POST["password2"]:
            user_password = request.POST["password1"]
        else:
            error = "Пароли должны совпадать!"
            header_secret_number = 5
            return render(request, 'main/registration.html', {"header_secret_number": header_secret_number,
                                                              "error": error})
        user_login = request.POST["username"]
        # for element in user.objects.all():
        for element in user.objects.raw('SELECT * FROM main_user'):
            if element.login == user_login:
                error = "Этот логин уже занят!"
                header_secret_number = 5
                return render(request, 'main/registration.html', {"header_secret_number": header_secret_number,
                                                                  "error": error})
        user_address = request.POST["address"]
        user_phone = request.POST["phone"]
        # for element in user.objects.all():
        for element in user.objects.raw('SELECT * FROM main_user'):
            if element.phone == user_phone:
                error = "На этот телефон уже зарегистрирован аккаунт!"
                header_secret_number = 5
                return render(request, 'main/registration.html', {"header_secret_number": header_secret_number,
                                                                  "error": error})
        user_name = request.POST["name"]
        user_role = role.objects.get(name="Пользователь")
        new_user = user(login=user_login, password=user_password,
                        name=user_name, phone=user_phone,
                        address=user_address, role_id=user_role)
        try:
            new_user.full_clean()
        except ValidationError as e:
            header_secret_number = 1
            return render(request, 'main/main.html', {"header_secret_number": header_secret_number,
                                                      "username_login": request.session['user_login']})
        new_user.save()
        header_secret_number = 1
        request.session['user_login'] = user_login
        return render(request, 'main/main.html', {"header_secret_number": header_secret_number,
                                                  "username_login": request.session['user_login']})
    else:
        return redirect('log_in')


def registration(request):
    header_secret_number = 5
    return render(request, 'main/registration.html', {"header_secret_number": header_secret_number})


@csrf_exempt
def change_user_data(request):
    if request.method == 'POST':
        if "username" in request.POST:
            # for element in user.objects.all():
            for element in user.objects.raw('SELECT * FROM main_user'):
                if element.login == request.POST["username"]:
                    error = "Этот логин уже занят!"
                    header_secret_number = 5
                    # user_data = user.objects.filter(login=request.session['user_login'])
                    lname = request.session['user_login']
                    user_data = user.objects.raw('SELECT * FROM main_user WHERE login = %s', [lname])
                    return render(request, 'main/profile.html', {"header_secret_number": header_secret_number,
                                                                 "username_login": request.session['user_login'],
                                                                 "user_data": user_data, "error": error})
            user_data = user.objects.get(login=request.session['user_login'])
            user_data.login = request.POST["username"]
            request.session['user_login'] = request.POST["username"]
            user_data.save()
        elif "address" in request.POST:
            user_data = user.objects.get(login=request.session['user_login'])
            user_data.address = request.POST["address"]
            user_data.save()
        elif "phone" in request.POST:
            # for element in user.objects.all():
            for element in user.objects.raw('SELECT * FROM main_user'):
                if element.phone == request.POST["phone"]:
                    error = "На этот телефон уже зарегистрирован аккаунт!"
                    header_secret_number = 5
                    # user_data = user.objects.filter(login=request.session['user_login'])
                    lname = request.session['user_login']
                    user_data = user.objects.raw('SELECT * FROM main_user WHERE login = %s', [lname])
                    return render(request, 'main/profile.html', {"header_secret_number": header_secret_number,
                                                                 "username_login": request.session['user_login'],
                                                                 "user_data": user_data, "error": error})
            user_data = user.objects.get(login=request.session['user_login'])
            user_data.phone = request.POST["phone"]
            user_data.save()
        elif "name" in request.POST:
            user_data = user.objects.get(login=request.session['user_login'])
            user_data.name = request.POST["name"]
            user_data.save()
        elif "password1" in request.POST:
            if request.POST["password1"] == request.POST["password2"]:
                user_data = user.objects.get(login=request.session['user_login'])
                user_data.password = request.POST["password1"]
                user_data.save()
            else:
                error = "Пароли должны совпадать!"
                header_secret_number = 5
                # user_data = user.objects.filter(login=request.session['user_login'])
                lname = request.session['user_login']
                user_data = user.objects.raw('SELECT * FROM main_user WHERE login = %s', [lname])
                return render(request, 'main/profile.html', {"header_secret_number": header_secret_number,
                                                             "username_login": request.session['user_login'],
                                                             "user_data": user_data, "error": error})
        return redirect('profile')
    else:
        return redirect('profile')


def log_out(request):
    request.session['user_login'] = ""
    return redirect('main')


def profile(request):
    header_secret_number = 5
    # user_data = user.objects.filter(login=request.session['user_login'])
    lname = request.session['user_login']
    user_data = user.objects.raw('SELECT * FROM main_user WHERE login = %s', [lname])
    user_role = user_data[0].role_id.name
    return render(request, 'main/profile.html', {"header_secret_number": header_secret_number,
                                                 "username_login": request.session['user_login'],
                                                 "user_data": user_data, "user_role": user_role})


@csrf_exempt
def log_in_check(request):
    header_secret_number = 5
    if request.method == 'POST':
        username = request.POST["username"]
        # if user.objects.filter(login=username):
        lname = username
        if user.objects.raw('SELECT * FROM main_user WHERE login = %s', [lname]):
            password = request.POST["password"]
            if user.objects.filter(login=username, password=password):
                request.session['user_login'] = username
                return redirect('/main')
            else:
                error = "Логин или пароль введён неправильно!"
                return render(request, 'main/log_in.html',
                              {"header_secret_number": header_secret_number, "error": error})
        else:
            error = "Логин или пароль введён неправильно!"
            return render(request, 'main/log_in.html', {"header_secret_number": header_secret_number, "error": error})
    else:
        return render(request, 'main/log_in.html', {"header_secret_number": header_secret_number})


def log_in(request):
    header_secret_number = 5
    return render(request, 'main/log_in.html', {"header_secret_number": header_secret_number})


def contact(request):
    header_secret_number = 4
    return render(request, 'main/contact.html', {"header_secret_number": header_secret_number,
                                                 "username_login": request.session['user_login']})


def delivery(request):
    header_secret_number = 3
    return render(request, 'main/delivery.html', {"header_secret_number": header_secret_number,
                                                  "username_login": request.session['user_login']})


def market(request):
    products_in_cart = []
    sum_cost = 0
    # products = product.objects.all()
    products = product.objects.raw('SELECT * FROM main_product')
    if 'cart' in request.session:
        for element in request.session['cart']:
            for element2 in products:
                if element == str(element2.id):
                    products_in_cart.append(element2)
                    break
        for element in products_in_cart:
            sum_cost += element.price
    # user_data = user.objects.filter(login=request.session['user_login'])
    lname = request.session['user_login']
    user_data = user.objects.raw('SELECT * FROM main_user WHERE login = %s', [lname])
    header_secret_number = 2
    if request.method == 'POST':
        # products = product.objects.filter(name=request.POST["number"])
        lname = request.POST["number"]
        products = product.objects.raw('SELECT * FROM main_product WHERE name = %s', [lname])
    return render(request, 'main/market.html', {"header_secret_number": header_secret_number,
                                                'products': products, "username_login": request.session['user_login'],
                                                'products_in_cart': products_in_cart,
                                                'sum_cost': sum_cost, "user_data": user_data})


def delete_product_in_cart(request, change):
    for element in range(len(request.session['cart'])):
        if request.session['cart'][element] == change:
            request.session['cart'].pop(element)
            break
    request.session.modified = True
    return JsonResponse({'foo': change})


def main(request):
    header_secret_number = 1
    return render(request, 'main/main.html', {"header_secret_number": header_secret_number,
                                              "username_login": request.session['user_login']})


def new_main(request):
    request.session['user_login'] = ""
    header_secret_number = 1
    return render(request, 'main/main.html', {"header_secret_number": header_secret_number,
                                              "username_login": request.session['user_login']})


def test(request):
    # # not_real_u = r.values_list('user_id', flat=True).distinct()
    # # u = user.objects.filter(id__in=not_real_u)
    # # big_request = list(chain(u, r))
    # if request.method == 'POST':
    #     # p_t = product_type.objects.get(name=request.POST['number'])
    #     # p = product.objects.filter(product_type_id=p_t)
    #     # r_h_p = receipt_has_product.objects.filter(product_id__in=p)
    #     # not_real_r = r_h_p.values_list('receipt_id', flat=True).distinct()
    #     # r = sorted(receipt.objects.filter(id__in=not_real_r), key=attrgetter('sum_cost'), reverse=True)
    #     r = sorted(receipt.objects.filter(id__in=receipt_has_product.objects.filter(
    #         product_id__in=product.objects.filter(
    #             product_type_id=product_type.objects.get(name=request.POST['number']))).values_list('receipt_id',
    #                                                                                                 flat=True).distinct()),
    #                key=attrgetter('sum_cost'), reverse=True)
    #     return render(request, 'main/test.html', {'big_request': r, 'type': request.POST['number']})
    # else:
    #     return render(request, 'main/test.html')
    # p_t = product_type.objects.get(animal=request.POST['number'])
    # p = product.objects.filter(animal="Кошка")
    # r_h_p = receipt_has_product.objects.filter(product_id__in=p)
    # not_real_r = r_h_p.values_list('receipt_id', flat=True).distinct()
    r = sorted(receipt.objects.filter(
        id__in=receipt_has_product.objects.filter(product_id__in=product.objects.filter(animal="Кошка")).values_list(
            'receipt_id', flat=True).distinct()), key=attrgetter('sum_cost'))
    all_receipt_has_product = receipt_has_product.objects.raw('SELECT * FROM main_receipt_has_product')
    return render(request, 'main/test.html', {'big_request': r, 'all_receipt_has_product': all_receipt_has_product})
