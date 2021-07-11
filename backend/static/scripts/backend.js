function displayView() {
    let post = JSON.parse(document.getElementById('post').textContent);
    let compare = JSON.parse(document.getElementById('compare_flag').textContent);
    let up = document.getElementById("upload");
    let im = document.getElementById("view");
    if (post === "Yes") {
        Cookies.set('uploaded', 'yes')
    }
    if (Cookies.get('uploaded', 'yes') === "yes") {
        up.style.display = "none";
        im.style.display = "flex";
        let bin = parseInt(JSON.parse(document.getElementById('bin_water').textContent));
        let est = parseInt(JSON.parse(document.getElementById('est_water').textContent));
        let binb = document.getElementById("bin_but");
        let estb = document.getElementById("est_but");
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
        if(compare==="Yes") {
            binb.style.background = "white";
            binb.innerText = "None";
            binb.style.color="black";
            estb.style.background = "white";
            estb.innerText = "None";
            estb.style.color="black";
            document.getElementById("bef_img_title").innerText="Before Flood Image";
            document.getElementById("comp").style.display="block";
            let bin_diff = parseInt(JSON.parse(document.getElementById('bin_water_diff').textContent));
            let est_diff  = parseInt(JSON.parse(document.getElementById('est_water_diff').textContent));
            let binb_com = document.getElementById("bin_but_com");
            let estb_com = document.getElementById("est_but_com");


            if(bin_diff>0){
                document.getElementById("comp_bin_text").innerText = "Change in water percentage : Increased by "+bin_diff+"%";
            }
            if(bin_diff<0){
                document.getElementById("comp_bin_text").innerText = "Change in water percentage : Decreased by "+bin_diff+"%";
            }
            if(bin_diff===0) {
                document.getElementById("comp_bin_text").innerText = "Change in water percentage : Unchanged";
            }
            if(est_diff>0){
                document.getElementById("comp_est_text").innerText = "Change in water percentage : Increased by "+est_diff+"%";
            }
            if(est_diff<0){
                document.getElementById("comp_est_text").innerText = "Change in water percentage : Decreased by "+est_diff+"%";
            }
            if(est_diff===0){
                document.getElementById("comp_est_text").innerText = "Change in water percentage : Unchanged";
            }


            if (bin_diff <= 10) {
                binb_com.style.background = "green";
                binb_com.innerText = "Low";
            }
            if (bin_diff > 10) {
                binb_com.style.background = "yellow";
                binb_com.innerText = "Medium";
            }
            if (bin_diff > 35) {
                binb_com.style.background = "orange";
                binb_com.innerText = "High";
            }
            if (bin_diff > 60) {
                binb_com.style.background = "red";
                binb_com.innerText = "Very High";
            }

            if (est_diff <= 10) {
                estb_com.style.background = "green";
                estb_com.innerText = "Low";
            }
            if (est_diff > 10) {
                estb_com.style.background = "yellow";
                estb_com.innerText = "Medium";
            }
            if (est_diff > 35) {
                estb_com.style.background = "orange";
                estb_com.innerText = "High";
            }
            if (est_diff > 60) {
                estb_com.style.background = "red";
                estb_com.innerText = "Very High";
            }
            
        }
    }

    let btn1 = document.querySelector("#b1");
    let btn2 = document.querySelector("#b2");
    let btn3 = document.querySelector("#b3");

    let btn4 = document.querySelector("#b1_com");
    let btn5 = document.querySelector("#b2_com");
    let btn6 = document.querySelector("#b3_com");

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
     btn4.addEventListener("click", function () {

        this.classList.add('btn_o-progress');
        setTimeout(function () {
            btn4.classList.add('btn_o-fill')
        }, 300);

        setTimeout(function () {
            btn4.removeClass('btn_o-fill')
        }, 2000);

        setTimeout(function () {
            btn4.classList.add('btn_o-complete')
        }, 2000);

    });
    btn5.addEventListener("click", function () {

        this.classList.add('btn_o-progress');
        setTimeout(function () {
            btn5.classList.add('btn_o-fill')
        }, 300);

        setTimeout(function () {
            btn5.removeClass('btn_o-fill')
        }, 2000);

        setTimeout(function () {
            btn5.classList.add('btn_o-complete')
        }, 2000);

    });
    btn6.addEventListener("click", function () {

        this.classList.add('btn_o-progress');
        setTimeout(function () {
            btn6.classList.add('btn_o-fill')
        }, 300);

        setTimeout(function () {
            btn6.removeClass('btn_o-fill')
        }, 2000);

        setTimeout(function () {
            btn6.classList.add('btn_o-complete')
        }, 2000);

    });


}

function icon_color() {
    let ax = document.getElementById("ic")
    ax.style.color = "#09A2FF"
}

function icon_color2() {
    let ax = document.getElementById("ic")
    ax.style.color = "white"
}

function toggle() {
    let up = document.getElementById("upload");
    let im = document.getElementById("view");
    let bu = document.getElementById("but");
    let ret = document.getElementById("ret");
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
    let up = document.getElementById("upload");
    let im = document.getElementById("view");
    let bu = document.getElementById("but");
    let ret = document.getElementById("ret");

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
    let element = document.getElementById("reseti");
    if (e === "1") {
        element.classList.add("fa-spin");
    }
    if (e === "2") {
        element.classList.remove("fa-spin");
    }
}

function show_compare(){
    if(document.getElementById("compare").style.display==="none")   {
        document.getElementById("bef_title").innerText="Select an Before flood image"
        document.getElementById("compare").style.display="block";
    }
    else    {
        document.getElementById("bef_title").innerText="Select an image"
        document.getElementById("compare").style.display="none";
    }
}
