#! /usr/bin/perl
require './jcode.pl';
require './sub.cgi';
require './conf.cgi';
&decode;
$date=time();
open(IN,"./data/guest_list.cgi");
@gue = <IN>;
close(IN);
$guest=@gue;
#if($guest>$LMAX){&error2("參加人數已達上限!");}
if($guest>$LMAX*0.9 && $in{'gm'} ne"1"){&login2;}
else{&login;}

sub login{
	&header;

print <<"EOF";
<BR>
<BR>
<CENTER>
$date
<form action="login2.cgi" method="POST">
<TABLE border="0" width="400" CLASS=FC>
  <TBODY>
    <TR>
      <TD bgcolor=$FCOLOR colspan=2 align=center><font size=3 color=$FCOLOR2>登入畫面</font></TD>
    </TR>
    <TR>
      <TD width="56" align=right>帳號</TD>
      <TD width="46"><input type=text size=15 name=id></TD>
    </TR>
    <TR>
      <TD width="56" align=right>密碼</TD>
      <TD width="46"><input type=password size=15 name=pass></TD>
    </TR>
    <TR>
      <TD colspan="2" align=center><font color=red><b>使用簡體中文的玩家請注意，請在公頻或國頻發言時先將字體轉為繁體字再進行發言，感謝</b></font></TD>
    </TR>
    <TR>
      <TD colspan="2" align=center>[<a href=/del_chara.html>刪除分身</a><BR><font color=red><b>如果你的帳號無法登入,請先確認下方「紀錄」中的「外掛紀錄」是不是有自己的名字,如果有,表示已被砍帳號</TD>
    </TR>
    <TR>
      <TD colspan="2" align=center><input type=submit CLASS=FC value=登入></TD>
    </TR>
  </TBODY>
</TABLE>
</CENTER>
</form>
EOF
	&mainfooter;
	exit;
}

sub login2{
	&header;

	open(IN,"./data/apo.cgi");
	@apo = <IN>;
	close(IN);
	&host_name;
	$timer = time();@newapo=();
	foreach(@apo) {
		($gname,$gid,$gtime)=split(/<>/);
		$time=300+$gtime-$timer;
		if($time>0){
			$guest2.="$gname($time秒後登入)<BR>";
		}else{
			$guest2.="<font color=red>$gname(登入可\能\)</font><BR>";
		}
	}

print <<"EOF";
<CENTER>
<TABLE border="0" width="100%" CLASS=FC>
  <TBODY>
    <TR>
      <TD bgcolor=$FCOLOR colspan=2 align=center><font size=3 color=$FCOLOR2>負荷上限防止機置啟動</font></TD>
    </TR>
    <TR>
      <TD width="100%" colspan=2 align=center>目前上限人數已達上限,請3分鐘後重試。</TD>
    </TR>
  </TBODY>
</TABLE>

<form action="login3.cgi" method="POST">

<TABLE border="0" width="300" CLASS=FC>
  <TBODY>
    <TR>
      <TD bgcolor=$FCOLOR colspan=2 align=center><font size=3 color=$FCOLOR2>排隊畫面</font></TD>
    </TR>
    <TR>
      <TD width="200" align=right>匿稱</TD>
      <TD width="100"><input type=text size=15 name=name></TD>
    </TR>
    <TR>
      <TD width="200" align=right>帳號</TD>
      <TD width="100"><input type=text size=15 name=id></TD>
    </TR>
    <TR>
      <TD colspan="2" align=center><input type=submit CLASS=FC value=\排\隊></TD>
    </TR>
  </TBODY>
</TABLE>
</form>
<TABLE border="0" width="500" CLASS=FC>
  <TBODY>
    <TR>
      <TD bgcolor=$FCOLOR colspan=2 align=center><font size=3 color=$FCOLOR2>\排\隊者一覽</font></TD>
    </TR>
    <TR>
      <TD bgcolor=$FCOLOR2 colspan=2 align=center><font size=3 color=$FCOLOR>$guest2</font></TD>
    </TR>
  </TBODY>
</TABLE>
<form action="login4.cgi" method="POST">
<TABLE border="0" width="300" CLASS=FC>
  <TBODY>
    <TR>
      <TD bgcolor=$FCOLOR colspan=2 align=center><font size=3 color=$FCOLOR2>登入畫面</font></TD>
    </TR>
    <TR>
      <TD width="56" align=right>ID</TD>
      <TD width="46"><input type=text size=15 name=id></TD>
    </TR>
    <TR>
      <TD width="56" align=right>PASS</TD>
      <TD width="46"><input type=password size=15 name=pass></TD>
    </TR>
    <TR>
      <TD colspan="2" align=center><input type=submit CLASS=FC value=登入></TD>
    </TR>
    <TR>
      <TD colspan="2" align=center>
<font color=red><b>使用簡體中文的玩家請注意，請在公頻或國頻發言時先將字體轉為繁體字再進行>發言，感謝</b></font>
</TD>
    </TR>

    <TR>
      <TD colspan="2" align=center>目前系統正在清理多於人員，如果你有沒在用的帳號或分身帳號，請先回到首頁的右上方[<a href=/del_chara.html>刪除分身</a>]將分身刪除，自行刪除者不再追究，如果遲不刪除，將GM查核有分身者，將於本尊連坐</TD>
    </TR>
  </TBODY>
</TABLE>
</CENTER>
</form>
</CENTER>
EOF
	&mainfooter;
	exit;
}
