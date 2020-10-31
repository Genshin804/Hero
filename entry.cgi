#! /usr/bin/perl
require './jcode.pl';
require './sub.cgi';
require './conf.cgi';

&decode;

if($CHARA_ENT){&error2("目前無法建立帳號。");}
##キャラ画像選択
$chlist="<select name=img>";
for($i=1;$i<=$CHARAIMG;$i++){
	$chlist.="<option value=$i>No.$i";
}
$chlist.="</select>";

##屬性選択
$j=0;
$elelist="<select name=ele>";
$elelist.="<option>-請選擇角色屬性-";
foreach(@ELE){
	$elelist.="<option value=$j>$ELE[$j]";
	$j++;
}
$elelist.="</select>";

##所屬國選択
$k=0;
open(IN,"./data/country.cgi") or &error2("國家文件無法開啟。");
@CON = <IN>;
close(IN);

$conlist="<select name=con_id>";
#$conlist.="<option>請選擇所屬國家";
$conlist.="<option value=0>無所屬";
$conlist.="</select>";

if($ATTESTATION){$mailcom="<BR><font color=red size=2>入力したアドレス宛に認証パスワードがメールにて送られます。登録後、入力したメールアドレス宛に届くメールに記載されたパスワードで認証を行う事で登録完了となります。<BR>メールアドレスが正しくない場合、認証メールが届かず登録できません。又、再度登録することもできませんのでご注意下さい。</font>";}

&header;

print <<"EOF";
<script language="JavaScript">
function changeImg(){
  	num=document.para.img.selectedIndex+1;
  	document.Img.src="$IMG/chara/"+ num +".gif";
}
</script>
<CENTER>
<form action="./chara_make.cgi" name=para method="POST">
<TABLE border="0" width="700" height="500" class=TC>
  <TBODY>
    <TR>
      <TD colspan="2" bgcolor="$FCOLOR" align="center"><FONT size="+2"><B><FONT color="#ffffcc" size="+2">建立新的角色</FONT></B></FONT></TD>
    </TR>
    <TR>
      <TD colspan="2" bgcolor="#ffffcc">※建立你的角色。<BR>
	※請特別注意:帳號、密碼、電子郵件請輸入正確。輸入錯誤將造成無法登入。<BR>
	<font color=red>※禁止開分身,若發現開分身,將會被禁止登入遊戲。</font>
      </TD>
    </TR>
    <TR>
      <TD bgcolor="#ffffcc">角色名稱</TD>
      <TD bgcolor="#ffffcc"><INPUT size=30 name=name><BR>
      ※請使用全形２～８個字(或半形４～１６個字)</TD>
    </TR>
    <TR>
      <TD bgcolor="#ffffcc">帳號</TD>
      <TD bgcolor="#ffffcc"><INPUT size=20 name=id><BR>
      ※帳號請使用４～８個半形字</TD>
    </TR>
    <TR>
      <TD bgcolor="#ffffcc">密碼</TD>
      <TD bgcolor="#ffffcc"><INPUT type=password size=20 name=pass><BR>
      ※密碼請使用４～８個半形字</TD>
    </TR>
    <TR>
      <TD bgcolor="#ffffcc">Email</TD>
      <TD bgcolor="#ffffcc"><INPUT type=text size=20 name=mail value=@><BR>
      ※請輸入你的Email $mailcom</TD>
    </TR>
   <TR>
      <TD bgcolor="#ffffcc">Email（確認用）</TD>
      <TD bgcolor="#ffffcc"><INPUT type=text size=20 name=mailconfirm value=@><BR>
      ※請再度輸入你的Email。</TD>
    </TR>
    <TR>
      <TD bgcolor="#ffffcc">角色圖案</TD>
	     <TD bgcolor="#ffffcc"><img src=\"$IMG/chara/1.gif\" name=\"Img\"><BR>
	   <select name=img onChange=\"changeImg()\">
EOF
	foreach (0..$CHARAIMG){
		if ($_ > 0){print "<option value=\"$_\">圖案[$_]\n";}
	}

	print <<"EOF";
	</select><br>請選擇角色的圖案。</TD>
    </TR>
    <TR>
      <TD bgcolor="#ffffcc">性別</TD>
      <TD bgcolor="#ffffcc"><select name="sex"><option value="0">男性<option value="1">女性</select></TD>
    </TR>
    <TR>
      <TD bgcolor="#ffffcc">屬性</TD>
      <TD bgcolor="#ffffcc">$elelist</TD>
    </TR>
<input type=hidden name=con_id value=0>
<!--
    <TR>
      <TD bgcolor="#ffffcc">所屬國家</TD>
      <TD bgcolor="#ffffcc">$conlist</TD>
    </TR>
-->
    <TR>
      <TD colspan="2" bgcolor="#ffffcc" align="center"><input type="submit"CLASS=FC value="建立角色"></TD>
    </TR>
  </TBODY>
  </form>
</TABLE>
</CENTER>
EOF

&mainfooter;
exit;

