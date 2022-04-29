  const cart_action_btns = document.querySelectorAll("#cart-action")


  function updateCart(data, reload) {
    if(reload === "yes") {
      window.location.reload();
    }
    const cart_item_count = data.cart_items
    const cart_item_text = document.getElementById("cart-items")
    cart_item_text.innerHTML = `Cart(${cart_item_count})`
   }

  function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== "") {
      var cookies = document.cookie.split(";");
      for (var i = 0; i < cookies.length; i++) {
        var cookie = cookies[i].trim();
        if (cookie.substring(0, name.length + 1) === name + "=") {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
 }

  if(cart_action_btns) {
    cart_action_btns.forEach((btn) => {
      btn.addEventListener("click", () => {
        const action = btn.dataset.action
        const id = btn.dataset.product
        const reload = btn.dataset.reload
        fetch('http://localhost:8000/api/orders/cart/add/', {
          headers : {'Content-Type' : 'application/json' , 'X-CSRFToken': getCookie('csrftoken')},
          method : 'POST',
          body : JSON.stringify(
            {
              id : id,
              action : action
            }
          )
        })

        .then((res) => {
          return res.json();
        })

        .then((data) => {
          if(reload) {
            updateCart(data, reload);
          }
          updateCart(data, "no")
        })
      })
    })
  }
  function fetchData() {
    fetch('http://localhost:8000/api/orders/cart/')
    .then((res) => {
      return res.json()
    })

    .then((data) => {
       updateCart(data);
    })
  }

  fetchData();