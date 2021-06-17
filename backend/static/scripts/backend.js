function displayView(bin1, est1) {
    var post = JSON.parse(document.getElementById('post').textContent);
    var up = document.getElementById("upload");
    var im = document.getElementById("view");

    if (post === "Yes") {
        Cookies.set('uploaded', 'yes')
    }
    if (Cookies.get('uploaded', 'yes') === "yes") {
        up.style.display = "none";
        im.style.display = "flex";
        var bin = parseInt(bin1)
        var est = parseInt(est1)
        binb = document.getElementById("bin_but");
        if (bin <= 25) {
            binb.style.background = "green";
            binb.innerText = "Low";
        }
        if (bin > 25) {
            binb.style.background = "yellow";
            binb.innerText = "Medium";
        }
        if (bin > 50) {
            binb.style.background = "orange";
            binb.innerText = "High";
        }
        if (bin > 75) {
            binb.style.background = "red";
            binb.innerText = "Very High";
        }
        estb = document.getElementById("est_but");
        if (est <= 25) {
            estb.style.background = "green";
            estb.innerText = "Low";
        }
        if (est > 25) {
            estb.style.background = "yellow";
            estb.innerText = "Medium";
        }
        if (est > 50) {
            estb.style.background = "orange";
            estb.innerText = "High";
        }
        if (est > 75) {
            estb.style.background = "red";
            estb.innerText = "Very High";
        }
    }

    var btn1 = document.querySelector("#b1");
    var btn2 = document.querySelector("#b2");
    var btn3 = document.querySelector("#b3");

    btn1.addEventListener("click", function () {

        this.classList.add('btn_o-progress');
        setTimeout(function () {
            btn1.classList.add('btn_o-fill')
        }, 300);

        setTimeout(function () {
            btn1.removeClass('btn_o-fill')
        }, 2000);

        setTimeout(function () {
            btn1.classList.add('btn_o-complete')
        }, 2000);

    });
    btn2.addEventListener("click", function () {

        this.classList.add('btn_o-progress');
        setTimeout(function () {
            btn2.classList.add('btn_o-fill')
        }, 300);

        setTimeout(function () {
            btn2.removeClass('btn_o-fill')
        }, 2000);

        setTimeout(function () {
            btn2.classList.add('btn_o-complete')
        }, 2000);

    });
    btn3.addEventListener("click", function () {

        this.classList.add('btn_o-progress');
        setTimeout(function () {
            btn3.classList.add('btn_o-fill')
        }, 300);

        setTimeout(function () {
            btn3.removeClass('btn_o-fill')
        }, 2000);

        setTimeout(function () {
            btn3.classList.add('btn_o-complete')
        }, 2000);

    });
}

function icon_color() {
    var ax = document.getElementById("ic")
    ax.style.color = "#09A2FF"
}

function icon_color2() {
    var ax = document.getElementById("ic")
    ax.style.color = "white"
}

function toggle() {
    var up = document.getElementById("upload");
    var im = document.getElementById("view");
    var bu = document.getElementById("but");
    var ret = document.getElementById("ret");
    if (up.style.display === "none") {
        bu.style.display = "block";
        ret.style.display = "block";
        up.style.display = "block";
        im.style.display = "none";
    } else {
        up.style.display = "none";
        im.style.display = "flex";
    }
}

function reset1() {
    var up = document.getElementById("upload");
    var im = document.getElementById("view");
    var bu = document.getElementById("but");
    var ret = document.getElementById("ret");

    Cookies.set('uploaded', 'no');
    bu.style.display = "none";
    ret.style.display = "none";
    up.style.display = "block";
    im.style.display = "none";

}

function download(url) {
    const a = document.createElement('a');
    a.href = url;
    a.download = url.split('/').pop() || 'download';
    const clickHandler = () => {
        setTimeout(() => {
            URL.revokeObjectURL(url);
            this.removeEventListener('click', clickHandler);
        }, 150);
    };
    a.addEventListener('click', clickHandler, false);
    setTimeout(function () {
        a.click();
        document.body.removeChild(a);
    }, 2000);
}

function reseth(e) {
    var element = document.getElementById("reseti");
    if (e === "1") {
        element.classList.add("fa-spin");
    }
    if (e === "2") {
        element.classList.remove("fa-spin");
    }
}
