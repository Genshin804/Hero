#! /usr/bin/perl
require './jcode.pl';
require './sub.cgi';
require './conf.cgi';
&decode;
&header;

if($LINK1){$print="<a href=\"$LINKURL1\" TARGET=\"_top\"><FONT size=\"1\" color=\"#ffff99\">[$LINK1]</a>　";}
if($LINK2){$print.="<a href=\"$LINKURL2\" TARGET=\"_blank\"><FONT size=\"1\" color=\"#ffff99\">[$LINK2]</a>　";}
if($LINK3){$print.="<a href=\"$LINKURL3\" TARGET=\"_blank\"><FONT size=\"1\" color=\"#ffff99\">[$LINK3]</a>　";}
if($LINK4){$print.="<a href=\"$LINKURL4\" TARGET=\"_blank\"><FONT size=\"1\" color=\"#ffff99\">[$LINK4]</a>　";}
if($LINK5){$print.="<a href=\"$LINKURL5\" TARGET=\"_blank\"><FONT size=\"1\" color=\"#ffff99\">[$LINK5]</a>　";}
if($LINK6){$print.="<a href=\"$LINKURL6\" TARGET=\"_blank\"><FONT size=\"1\" color=\"#ffff99\">[$LINK6]</a>　";}
if($LINK7){$print.="<a href=\"$LINKURL7\" TARGET=\"_blank\"><FONT size=\"1\" color=\"#ffff99\">[$LINK7]</a>　";}
if($LINK8){$print.="<a href=\"$LINKURL8\" TARGET=\"_blank\"><FONT size=\"1\" color=\"#ffff99\">[$LINK8]</a>　";}
if($LINK9){$print.="<a href=\"$LINKURL9\" TARGET=\"_blank\"><FONT size=\"1\" color=\"#ffff99\">[$LINK9]</a>　";}
if($LINK10){$print.="<a href=\"$LINKURL10\" TARGET=\"_blank\"><FONT size=\"1\" color=\"#ffff99\">[$LINK10]</a>　";}
if($LINK11){$print.="<a href=\"$LINKURL11\" TARGET=\"_blank\"><FONT size=\"1\" color=\"#ffff99\">[$LINK11]</a>　";}
if($LINK12){$print.="<a href=\"$LINKURL12\" TARGET=\"_blank\"><FONT size=\"1\" color=\"#ffff99\">[$LINK12]</a>　";}
if($LINK13){$print.="<a href=\"$LINKURL13\" TARGET=\"_blank\"><FONT size=\"1\" color=\"#ffff99\">[$LINK13]</a>　";}
if($LINK14){$print.="<a href=\"$LINKURL14\" TARGET=\"_blank\"><FONT size=\"1\" color=\"#ffff99\">[$LINK14]</a>　";}

print <<"EOF";

<center>
<FONT size="1" color=\"#ffff99\">
$print
</center>
<SCRIPT LANGUAGE = "JavaScript">
function keyDownHandler(e) {
    if (e) { // Firefox
                e.preventDefault();
                e.stopPropagation();
    } else { // IE
                window.event.keyCode = 0;
                return false;
    }
}
document.onkeydown = keyDownHandler;
</script>
EOF
exit;
  
