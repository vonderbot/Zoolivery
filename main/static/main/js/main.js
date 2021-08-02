// основа
window.addEventListener('scroll', function() {
  if (document.getElementById("navigation_menu").getBoundingClientRect().bottom > 0) {
    document.getElementsByTagName("header")[0].style.display = "none";
  } else if (document.getElementById("navigation_menu").getBoundingClientRect().bottom <= 0) {
    document.getElementsByTagName("header")[0].style.display = "block";
  }
});
// магазин
  sum = sum.replace(',', '.');
  sum = Number(sum);

function show() {
  document.getElementById("bin_window").style.display = 'block';
  document.getElementById("gray").style.display = 'block';
}

if (a){
show()
}

function not_show() {
  document.getElementById("bin_window").style.display = 'none';
  document.getElementById("bin_window1").style.display = 'none';
  document.getElementById("window").style.display = 'none';
  document.getElementById("gray").style.display = 'none';
}

function buy(text, cost, id) {
  i++;
  var xhttp = new XMLHttpRequest();
  xhttp.open("GET", "backet_data_save/" + id, true);
  xhttp.send();
  cost = cost.replace(',', '.');
  cost = Number(cost);
  var new_div = document.createElement('div');
  var new_span = document.createElement('span');
  var new_font = document.createElement('font');
  var old_elem = document.getElementById('bin_window_window');
  new_div.className = 'bin_label';
  new_div.id = i;
  new_div.dataset.cost = cost;
  new_span.className = 'closebtn';
  new_span.textContent = '×';
  new_span.addEventListener('click', function(){delete_product_in_cart(id, i)});
  new_font.innerText = text;
  new_font.face = "RalewayRegular";
  new_font.size = "4";
  new_div.appendChild(new_font);
  new_div.appendChild(new_span);
  old_elem.appendChild(new_div);
  document.getElementById("bin_window").style.display = 'block';
  document.getElementById("gray").style.display = 'block';
  sum = Number(sum);
  sum = (sum + cost).toFixed(2);
  document.getElementById("sum_costs").innerText = "Общая цена: " + sum + " UAH";
}
function offer_start() {
document.getElementById("bin_window").style.display = 'none';
document.getElementById("bin_window1").style.display = 'block';
}
function change_input(){
if(document.getElementById("delivery_type").value == "Самовывоз"){
document.getElementById("Почта").style.display = 'none';
document.getElementById("Курьер").style.display = 'none';
document.getElementsByName("post_station_address")[0].removeAttribute("required");
document.getElementsByName("address")[0].removeAttribute("required");
document.getElementsByName("post_station_address")[0].value = ("");
document.getElementsByName("address")[0].value = ("");
}
else if(document.getElementById("delivery_type").value == "Почта"){
document.getElementById("Почта").style.display = 'block';
document.getElementById("Курьер").style.display = 'none';
document.getElementsByName("post_station_address")[0].required = true;;
document.getElementsByName("address")[0].removeAttribute("required");
document.getElementsByName("post_station_address")[0].value = ("");
document.getElementsByName("address")[0].value = ("");
}
else if(document.getElementById("delivery_type").value == "Курьер"){
document.getElementById("Почта").style.display = 'none';
document.getElementById("Курьер").style.display = 'block';
document.getElementsByName("post_station_address")[0].removeAttribute("required");
document.getElementsByName("address")[0].required = true;;
document.getElementsByName("post_station_address")[0].value = ("");
document.getElementsByName("address")[0].value = (address_value);
}
}

function delete_product_in_cart(ida, parent) {
  var xhttp = new XMLHttpRequest();
  xhttp.open("GET", "delete_product_in_cart/" + ida, true);
  xhttp.send();
  console.log(parent);
  var parent = document.getElementById(parent);
  var cost = parent.dataset.cost;
  parent.remove();
  cost = cost.replace(',', '.');
  cost = Number(cost);
  console.log(sum);
  console.log(Number(cost));
  sum = Number(sum);
  sum = (sum - cost).toFixed(2);
  document.getElementById("sum_costs").innerText = "Общая цена: " + sum + " UAH";
}
//скрипты страницы входа в аккаунт
function not_empty1() {
        if (document.getElementById("first_input").value.length >= 3) {
          document.getElementById('empty4').hidden = true;
        } else if (document.getElementById("first_input").value.length <= 3) {
          document.getElementById('empty4').hidden = false;
        }
        var flag = 0;
        for (var i = 0; i < 10; i++) {
          document.getElementById('empty5').hidden = true;
          for (var j = 0; j < document.getElementById("first_input").value.length; j++) {
            if (document.getElementById("first_input").value[j] != " ") {
              document.getElementById('empty5').hidden = true;
            } else if (document.getElementById("first_input").value[j] == " ") {
              document.getElementById('empty5').hidden = false;
              flag = 1;
              break;
            }
          }
          if (flag == 1) {
            break;
          }
        }
      }
function back() {
        document.getElementById('empty4').hidden = false;
        document.getElementById('empty5').hidden = true;
      }
//скрипты странички всех заказов(может видеть только курьер)
function change_status(id) {
a = document.getElementById(id).value;
b = document.getElementById(String(id)).dataset.receipt;
var xhttp = new XMLHttpRequest();
  xhttp.open("GET", "change_status/" + a +"/"+b, true);
  xhttp.send();
}