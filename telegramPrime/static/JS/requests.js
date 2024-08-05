const contactPopup = document.querySelector(".contact__popup__wrap");
const showHidePopup = (state) => {
  if (state == 0) {
    contactPopup.classList.add("show");
  } else {
    contactPopup.classList.remove("show");
  }
};

const scamPopup = document.querySelector(".scammer__warn__popup__wrap");

const hideScamPopup = (state) => {
  if (state == 0) {
    scamPopup.classList.add("hide");
  } else {
    scamPopup.classList.add("hide");
    showHidePopup(0);
  }
  document.cookie = "scamPopup=true;";
};

window.onload = () => {
  if (document.cookie.includes("scamPopup=true")) {
    return;
  }
  if (!document.cookie.includes("scamPopup=false")) {
    document.cookie = "scamPopup=false;";
    setTimeout(() => {
      scamPopup.classList.add("show");
    }, 2000);
  }
};

let formCancell = false;
const validation = () => {
  const inputs = document.querySelectorAll(".form__input");
  inputs.forEach((item) => {
    if (item.value == "") {
      formCancell = true;
      item.classList.add("incorrect__input");
    } else {
      formCancell = false;
      item.classList.remove("incorrect__input");
    }
  });
};

// let forms = 0
// const sendForm = async (state) => {

//   if (formCancell == false) {
//     forms += 1
//     event.preventDefault();
//     if (state == 0) {
//       showHidePopup(1);
//     }
//     if(forms == 1){
//       const contactData = document.querySelector(".contact__form");
//       return await fetch("https://jsonplaceholder.typicode.com/posts", {
//         method: "POST",
//         body: new FormData(contactData),
//       });
//     }
//   } else {
//     event.preventDefault();
//   }
// };

const submitForm = async (e) => {
  validation()
  if (!formCancell) {
    const formData = new FormData(e);
    const dataObject = {};
    formData.forEach((value, key) => {
      dataObject[key] = value;
    });
    await fetch("http://localhost:8000/feedback/", {
      method: "POST",
      data: JSON.stringify(dataObject),
    }).then(res => res.json()).then(res => {
      alert(1)
    }).catch(err => console.log(err))
  }
}