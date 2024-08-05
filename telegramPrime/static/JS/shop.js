const products = [
  {
    id: 1,
    name: "Название#1",
    img: "/static/IMG/firstTovar.png",
    description: "Описание #1",
    price: 2000,
  },
  {
    id: 2,
    name: "Название#2",
    img: "/static/IMG/secTovar.png",
    description: "Описание #2",
    price: 1000,
  },
  {
    id: 3,
    name: "Название#3",
    img: "/static/IMG/thirdTovar.png",
    description: "Описание #3",
    price: 1000,
  },
  {
    id: 4,
    name: "Название#4",
    img: "/static/IMG/firstTovar.png",
    description: "Описание #4",
    price: 5000,
  },
  {
    id: 5,
    name: "Название#5",
    img: "/static/IMG/firstTovar.png",
    description: "Описание #5",
    price: 1000,
  },
  {
    id: 6,
    name: "Название#6",
    img: "/static/IMG/firstTovar.png",
    description: "Описание #6",
    price: 1000,
  },
  {
    id: 7,
    name: "Название#7",
    img: "/static/IMG/firstTovar.png",
    description: "Описание #6",
    price: 1000,
  },
  {
    id: 8,
    name: "Название#8",
    img: "/static/IMG/firstTovar.png",
    description: "Описание #6",
    price: 1000,
  },
  {
    id: 9,
    name: "Название#9",
    img: "/static/IMG/firstTovar.png",
    description: "Описание #6",
    price: 1000,
  },
  {
    id: 10,
    name: "Название#10",
    img: "/static/IMG/firstTovar.png",
    description: "Описание #6",
    price: 1000,
  },
  {
    id: 11,
    name: "Название#11",
    img: "/static/IMG/firstTovar.png",
    description: "Описание #6",
    price: 1000,
  },
  {
    id: 12,
    name: "Название#12",
    img: "/static/IMG/firstTovar.png",
    description: "Описание #6",
    price: 1000,
  },
  {
    id: 13,
    name: "Название#13",
    img: "/static/IMG/firstTovar.png",
    description: "Описание #6",
    price: 1000,
  },
  {
    id: 14,
    name: "Название#14",
    img: "/static/IMG/firstTovar.png",
    description: "Описание #6",
    price: 1000,
  },
  {
    id: 15,
    name: "Название#15",
    img: "/static/IMG/firstTovar.png",
    description: "Описание #6",
    price: 1000,
  },
  {
    id: 16,
    name: "Название#16",
    img: "/static/IMG/firstTovar.png",
    description: "Описание #6",
    price: 1000,
  },
  {
    id: 17,
    name: "Название#17",
    img: "/static/IMG/firstTovar.png",
    description: "Описание #6",
    price: 1000,
  },
  {
    id: 18,
    name: "Название#18",
    img: "/static/IMG/firstTovar.png",
    description: "Описание #6",
    price: 1000,
  },
  {
    id: 19,
    name: "Название#19",
    img: "/static/IMG/firstTovar.png",
    description: "Описание #6",
    price: 1000,
  },
  {
    id: 20,
    name: "Название#20",
    img: "/static/IMG/firstTovar.png",
    description: "Описание #6",
    price: 1000,
  },
  {
    id: 21,
    name: "Название#21",
    img: "/static/IMG/firstTovar.png",
    description: "Описание #6",
    price: 1000,
  },
  {
    id: 22,
    name: "Название#22",
    img: "/static/IMG/firstTovar.png",
    description: "Описание #6",
    price: 1000,
  },
  {
    id: 23,
    name: "Название#23",
    img: "/static/IMG/firstTovar.png",
    description: "Описание #6",
    price: 1000,
  },
  {
    id: 24,
    name: "Название#24",
    img: "/static/IMG/firstTovar.png",
    description: "Описание #6",
    price: 1000,
  },
];

const displayProduct = () => {
  const productsBlock = document.querySelectorAll(".product");
  let productsImg = document.querySelectorAll(".product__img");
  let productsName = document.querySelectorAll(".product__name");
  let buyBtns = document.querySelectorAll(".buy__btn");

  for (let i = 0; i < productsBlock.length; i++) {
    if (+productsBlock[i].id == products[i].id) {
      productsName[i].innerHTML = products[i].name;
      productsImg[i].src = products[i].img;
      console.log(productsImg[i].src);
      buyBtns[i].innerHTML = `Купить: ${products[i].price + " ₽"}`;
    }
  }
};
displayProduct();

const showCard = (state) => {
  const cardPopup = document.querySelector(".choosen__products__wrap");
  if (state == 0) {
    cardPopup.classList.add("show__card");
  } else {
    cardPopup.classList.remove("show__card");
  }
};

let totalPrice = 0;
let productsArray = [];
let productNameSend;
const formCard = (id) => {
  const section = document.createElement("section");
  const img = document.createElement("img");
  const productName = document.createElement("p");
  const price = document.createElement("p");
  const productsItems = document.querySelector(".products__items");

  section.classList.add("item");
  img.src = products[id - 1].img; // img
  img.classList.add("card__product__img");
  productName.classList.add("product__name__input");
  productName.textContent = products[id - 1].name;
  productsArray.push(productName.textContent);
  productNameSend = document.createElement("input");
  productNameSend.type = "text";
  productNameSend.classList.add("hide__input");
  price.classList.add("card__product__price");
  price.textContent = products[id - 1].price + "₽"; // price

  section.appendChild(img);
  section.appendChild(productName);
  section.appendChild(price);
  section.appendChild(productNameSend);
  productsItems.appendChild(section);

  let productsPrice = document.querySelector(".products__price");
  totalPrice += products[id - 1].price;
  productsPrice.value = totalPrice + " ₽";
};

let sendState = true;
const paymentValidation = () => {
  sendState = true;
  const productInputs = document.querySelectorAll(".product__input");
  productInputs.forEach((input) => {
    if (input.value == "") {
      sendState = false;
      input.classList.add("cancell__form");
    } else {
      input.classList.remove("cancell__form");
    }
  });
};

const closePayment = (state) => {
  const paymentPopup = document.querySelector('.choosen__payment__system__wrap')
  if (state == 0) {
    paymentPopup.classList.remove('show')
  }
};

const sendPaymentData = async (state, id) => {
  event.preventDefault();
  switch (state) {
    case 0:
      if (sendState == true) {
        showCard(1);
        const chooseSystem = document.querySelector(
          ".choosen__payment__system__wrap"
        );
        chooseSystem.classList.add("show");

        productNameSend.name = "productName";
        productNameSend.value = productsArray;
      }
      break;
    case 1:
      const sendForm = new FormData(document.querySelector(".payment__form"));
      sendForm.append("id", id);
      return await fetch("http://localhost:8000/payments/create/", {
        method: "POST",
        body: sendForm,
      });
  }
};

const showDescription = (state, id) => {
  const descriptionPopup = document.querySelector(
    ".product__description__popup__wrap"
  );
  if (state == 0) {
    const popupDescriptionName = document.querySelector(
      ".product__description__name"
    );
    const popupDescriptionImg = document.querySelector(
      ".product__description__img"
    );
    const popupDescription = document.querySelector(
      ".product__description__description"
    );
    popupDescriptionName.innerHTML = products[id].name;
    popupDescriptionImg.src = products[id].img;
    popupDescription.innerHTML = products[id].description;
    descriptionPopup.classList.add("show");
  } else {
    descriptionPopup.classList.remove("show");
  }
};

const showPaymentTypes = () => {
  const chooseSystem = document.querySelector(
    ".choosen__payment__system__wrap"
  );
  chooseSystem.classList.add("show");
}

const createPayment = async () => {
  paymentValidation()
  if (sendState) {
    const formData = new FormData(e);
    const dataObject = {};
    formData.forEach((value, key) => {
      dataObject[key] = value;
    });
    await fetch("http://localhost:8000/payments/create/", {
      method: "POST",
      data: JSON.stringify({ ...dataObject, price: totalPrice, productName: productsArray, id: 1 }),
    }).then(res => res.json()).then(res => {
      alert(1)
      window.open(res.url, "_self")
    }).catch(err => console.log(err))
  }
}