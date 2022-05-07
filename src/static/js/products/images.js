const images = document.querySelectorAll(".sub-image")
const main_image = document.getElementById("main")

if(images) {
    images.forEach((image) => {
        image.addEventListener("click", () => {
            main_image.src = image.src
        })
    })
}