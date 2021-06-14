function switch_cam() {
    var frame = document.getElementById("camera_view");
    if (frame.src=="http://192.168.29.244:8080/browserfs.html") {
        frame.src = "https://www.youtube.com/embed/U6qbhBln7jE";
    }
    else {
        frame.src="http://192.168.29.244:8080/browserfs.html"
    }
}