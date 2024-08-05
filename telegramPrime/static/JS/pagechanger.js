function changePage(id) {
  localStorage.setItem("selectedBlockId", id);
  window.location.href = "knowbase.html";
}

function changeModule(id, state) {
  if (state == 1) {
    localStorage.setItem("selectedModuleId", id);
    window.location.href = "module.html";
  }
}
