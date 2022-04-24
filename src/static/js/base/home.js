const root = document.getElementById("root")

function insertToRoot(data) {
    data.forEach((item) => {
        const card = document.createElement("div")
        const column = document.createElement("div")
        column.className = "col-sm mb-3"
        card.className = "card"
        const url = `/products/${item.id}/`
        const image_url = `${item.main_image}`

        card.innerHTML = `
        <img src=${image_url} class="card-img-top" alt="" style="width : 18rem;"/>
        <hr />
        <div class="card-body">
        <h4>${item.title}</h4>
        <p>$${item.price}</p>

        <a href=${url} class="btn btn-primary">View</a>
        </div>
        `
        column.appendChild(card)
        root.appendChild(column)
    })
}

function getProducts() {
    fetch('http://localhost:8000/api/products/')
    .then((res) => {
        return res.json();
    })

    .then((data) => {
        insertToRoot(data);
    })
}

getProducts();
