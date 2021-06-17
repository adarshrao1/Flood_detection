function switch_cam() {
    var frame = document.getElementById("camera_view");
    if (frame.src == "http://bit.do/floodvtol") {
        frame.src = "http://bit.do/floodvtol2";
    } else {
        frame.src = "http://bit.do/floodvtol"
    }
}