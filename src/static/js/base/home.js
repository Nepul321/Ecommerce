const root = document.getElementById("root")

function insertToRoot(data) {
    data.forEach((item) => {
        const card = document.createElement("div")
        card.className = "border p-3"

        card.innerHTML = `
        <h2>${item.title}</h2>
        <p>$${item.price}</p>

        <a href="" class="btn btn-info text-white">View</a>
        `

        root.appendChild(card)
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
