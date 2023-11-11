let colors = document.querySelectorAll('.give_color')

let click_color = document.querySelectorAll('.click')


for (let color of colors) {
    let get_color = color.innerText
    color.style.backgroundColor = `${get_color}`
    // color.innerText = ''
}

for (let i of click_color) jjj(i)

function fff(data) {
    sizes = document.getElementById('sizes')
    sizes.innerHTML = ''

    if (data?.data.length == 0) {
        span = document.createElement('b')
        span.innerText = 'No Product Left'
        sizes.append(span)
    } else {
        for (let i of data.data) {
            span = document.createElement('span')
            span.innerText = i.size
            span.classList.add('size')
            span.setAttribute("data_price", i?.add_or_subtract_price)
            sizes.append(span)
        }
    }
}

function get_request(id) {
    fetch(`/product/json/${id}`)
        .then((data) => data.json())
        .then((data) => fff(data))
        .catch((err) => console.log(err))
}

function kkk(i, click_size) {
    i.addEventListener('click', () => {
        for (let j of click_size) j.classList.remove('active')
        i.classList.toggle('active')
        let product_price = document.querySelector('.red')
        let product_price_atr = product_price.getAttribute('product-price')
        let total = parseFloat(product_price_atr) + parseFloat(i.getAttribute('data_price'))
        console.log(total)
        product_price.innerText = "$ " + total.toFixed(2)
    })
}

function hhh() {
    let click_size = document.querySelectorAll('.size')
    for (let i of click_size) {
        kkk(i, click_size)
    }
}

function jjj(i) {
    i.addEventListener('click', () => {
        for (let j of click_color) j.classList.remove('active')
        i.classList.toggle('active')
        get_request(i.id)

        setTimeout(() => {
            hhh()
        }, 100)
    })
}
