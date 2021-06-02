
let cover_pic = document.querySelector(".profile-container .profile-section-main .profile-section .profile-main-part .profile-part-cover-img img");
function cover_change(){
    randomNum = Math.floor(Math.random() * 6) + 1;
    randomImg = "default" + randomNum + ".jpg";
    cover_pic.src = `https://source.unsplash.com/featured/?aesthetic,nepal`
}
cover_change()