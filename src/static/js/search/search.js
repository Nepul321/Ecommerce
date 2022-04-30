const form = document.getElementById("searchForm");

form.addEventListener('submit', (e) => {
    e.preventDefault();
    const searched = e.target[1].value
    window.location.href = `/search?q=${searched}`
})