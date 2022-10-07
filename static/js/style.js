// NAVIGATION BAR
function openNavbarForMobile() {
    document.getElementById("nav-mobile").style.display = "flex";
    document.getElementById("nav-mobile").style.flexDirection = "column";
    document.getElementById("nav-mobile").style.justifyContent = "center";
    document.getElementById("nav-mobile").style.alignItems = "center";
    document.getElementById("nav-laptop").style.display = "none";
    document.querySelector("#nav-mobile li:nth-of-type(2)").style.margin =
        "0";
    document.querySelector('main').style.display = "none"
}
function closeNavbarForMobile() {
    document.getElementById("nav-mobile").style.display = "none";
    document.getElementById("nav-laptop").style.display = "flex";
    document.querySelector('main').style.display = "block"

}



