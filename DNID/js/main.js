function menuClick(x) {
    x.classList.toggle("change");
}

function openNav() {
    document.getElementById("mySidebar").style.width = "275px";
    document.getElementsByClassName("navbar").style.opacity = "0.6";
}
  
  function closeNav() {
    document.getElementById("mySidebar").style.width = "0";
    document.body.style.opacity = 1;
}
