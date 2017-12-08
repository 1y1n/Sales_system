
function chuku_card(form){//弹窗确定是否出库，还有填写操作人,售价等
    var shoujia = form.shoujia.value;
    var fkfs = form.fkfs.value;
    var ckrq = form.ckrq.value;
    var msg = "已经出库是否重新出库？\n\n请确认！"
    if(ckrq != 'None'){
        if (confirm(msg)==true){
        }
        else{
            return false;
        }
    }
    if(shoujia == 'None'){
        alert('售价不能为空');
        return false;}

    else if(fkfs == '' || fkfs== 'None'){
        alert('付款方式不能为空');
        return false;}

    alert("出库成功");
}


function chuku_gift(form){//弹窗确定是否出库，还有填写操作人,售价等
    var ckrq = form.ckrq.value;
    var msg = "已经出库是否重新出库？\n\n请确认！"
    if(ckrq != 'None'){
        if (confirm(msg)==true){
        }
        else{
            return false;
        }
    }
    alert("出库成功");
}

function chuku_mobile(form){//弹窗确定是否出库，还有填写操作人,售价等
    var shoujia = form.shoujia.value;
    var fkfs = form.fkfs.value;
    var ckrq = form.ckrq.value;
    var msg = "已经出库是否重新出库？\n\n请确认！"
    if(ckrq != 'None'){
        if (confirm(msg)==true){
        }
        else{
            return false;
        }
    }
    if(shoujia == 'None'){
        alert('售价不能为空');
        return false;}

    else if(fkfs == '' || fkfs == 'None'){
        alert('付款方式不能为空');
        return false;}

    alert("出库成功");
}

function chuku_parts(form){//弹窗确定是否出库，还有填写操作人,售价等
    var shoujia = form.shoujia.value;
    var fkfs = form.fkfs.value;
    var ckrq = form.ckrq.value;
    var msg = "已经出库是否重新出库？\n\n请确认！"
    if(ckrq != 'None'){
        if (confirm(msg)==true){
        }
        else{
            return false;
        }
    }
    if(shoujia == 'None'){
        alert('售价不能为空');
        return false;}

    else if(fkfs == '' || fkfs == 'None'){
        alert('付款方式不能为空');
        return false;}

    alert("出库成功");
}

function shanchu(){//弹窗确定是否删除

    var msg = "您真的确定要删除吗？\n\n请确认！"
    if (confirm(msg)==true){
        alert("删除成功");
        return true;
    }
    else{
        return false;
    }
}
