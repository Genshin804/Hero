#! /usr/bin/perl
require './jcode.pl';
require './sub.cgi';
require './conf.cgi';
require './attestation.cgi';

&decode;
&host_name;

if($CHARA_ENT){&error2("目前無法再新建帳號。");}
if($ENV{'HTTP_REFERER'} !~ /cgi$/ ){ &error2("請勿從外部連進入。"); }

if($in{'id'} eq ""){&error2("請輸入帳號!");}
if ($in{'name'} =~ / / || $in{'name'} =~ /GM/ || $in{'name'} =~ /ＧＭ/ || $in{'name'} =~/,/) {&error("名字中請不要出現空格豆號或ＧＭ等字樣。"); }
if($in{'pass'} eq $in{'id'}){&error2("帳號與密碼不可一樣!");}
if($in{'pass'} eq ""){&error2("請輸入密碼!");}
if(length($in{'id'}) < 4||length($in{'id'}) > 8){&error2("帳號請使用４～８個半形字");}
if(length($in{'pass'}) < 4||length($in{'pass'}) > 8){&error2("密碼請使用４～８個半形字");}
if($in{'id'} eq $in{'pass'}){&error2("帳號與密碼不可一樣!"); }	
if ($in{'id'} =~ m/[^0-9a-zA-Z]/) {&error2("帳號請使用半形文字"); }
if ($in{'pass'} =~ m/[^0-9a-zA-Z]/) {&error2("密碼請使用半形文字"); }
if($in{'name'} eq ""){&error2("請輸入角色名稱");}
if(length($in{'name'}) < 4||length($in{'name'}) > 32){&error2("角色名稱請使用全形２～８個字(或半形４～１６個字)");}
if($in{'sex'} eq ""){&error2("請選擇性別。");}
if($in{'img'} eq ""){&error2("請選擇角色圖案。");}
if($in{'ele'} eq ""){&error2("請選擇屬性。");}
if($in{'con_id'} eq ""){&error2("請選擇所屬國家。");}
#if ($in{'mail'} =~ /yahoo/ || $in{'mail'} =~ /hotmail/ || $in{'mail'} =~ /excite/ || $in{'mail'} =~ /infoseek/  || $in{'mail'} =~ /goo/) {&error2("そのメールアドレスは使用できません。"); }
if ($in{'mail'} eq "" || $in{'mail'} !~ /(.*)\@(.*)\.(.*)/){&error2("你的Email輸入有誤");}
if ($in{'mail'} ne $in{'mailconfirm'}){&error2("你的Email兩次輸入不一致");}
if($ATTESTATION){
	$os = 1;
}else{
	$os = "";
}
                $dir="./logfile/chara";
                opendir(dirlist,"$dir");
                while($file = readdir(dirlist)){
                        if($file =~ /\.cgi/i){
                                $datames = "查詢：$dir/$file<br>\n";
                                if(open(cha,"$dir/$file")){

                                @cha = <cha>;
                                close(cha);
                                $list[$i]="$file";
                                ($rid,$rpass,$rname,$rurl,$rchara,$rsex,$rhp,$rmaxhp,$rmp,$rmaxmp,$rele,$rstr,$rvit,$rint,$rfai,$rdex,$ragi,$rmax,$rcom,$rgold,$rbank,$rex,$rtotalex,$rjp,$rabp,$rcex,$runit,$rcon,$rarm,$rpro,$racc,$rtec,$rsta,$rpos,$rmes,$rhost,$rdate,$rsyo,$rclass,$rtotal,$rkati,$rtype) = split(/<>/,$cha[0]);
                                                        if($rname eq $in{'name'}){closedir(dirlist);&error2("「$rname」已被其
他玩家使用");}
                                }
                        }
                        if($mn>10000){&error("ループ");}
                        $mn++;
                }	
$id=$in{'id'};
$pass=$in{'pass'};
$hp=50;$mp=10;$str=20;$vit=20;$int=20;
$dex=20;$agi=20;$fai=20;
$gold=50;$ex=0;$cex=0;$bank=0;
$arm="0,新手木劍,0,0,0,0,80,10,0,0,0";
$pro="0,新手布衣,0,0,0,0,80,10,0,0,0";
$acc="0,新手指輪,0,0,0,0,80,10,0,0,0";
$tac="0,0,0,50,50";
$max="200,200,200,200,200,200";
$class=0;$kati=0;$total=0;$pos=0;
$pet="";
$date = time();
if($ATTESTATION){$mailcom="<BR><font color=red>※你的認證信將發送到你的Email信箱中。</font>";}

open(IN,"./data/country.cgi") or &error2("城市文件無法開啟。");
@CON_DATA = <IN>;
close(IN);

foreach(@CON_DATA){
	($con_id,$con_name,$con_ele)=split(/<>/);
	if("$con_id" eq "$in{'con_id'}"){$hit=1;last;}
}
if($in{'con_id'} ne 0 && !$hit){&error2("請正確選擇所屬國家。");}
if($in{'con_id'} eq 0){$con_name="無所屬";}

$dir="./logfile/chara";
opendir(dirlist,"$dir");
while($file = readdir(dirlist)){
	if($file =~ /\.cgi/i){
		$datames = "查詢：$dir/$file<br>\n";
		if(!open(chara,"$dir/$file")){
			&error("$dir/$file 找不到檔案。<br>\n");
		}
		@chara = <chara>;
		close(chara);
		$list[$i]="$file";
		($eid,$epass,$ename,$eurl,$echara,$esex,$ehp,$emaxhp,$emp,$emaxmp,$eele,$estr,$evit,$eint,$efai,$edex,$eagi,$emax,$ecom,$egold,$ebank,$eex,$etotalex,$ejp,$eabp,$ecex,$eunit,$econ,$earm,$epro,$eacc,$etec,$esta,$epos,$emes,$ehost,$edate,$esyo,$eclass,$etotal,$ekati,$etype,$eoya,$eaup,$eflg,$eflg2,$eflg3,$eflg4,$eflg5,$epet) = split(/<>/,$chara[0]);
	
		if($DOUBLE eq "1" && $ehost eq"$host"){
			&maplog3("<font color=red>[重複]</font><font color=blue>$in{'name'}</font>與<font color=blue>$ename</font>疑似為同一人。");
			&error2("同一個人無法建立兩個建號。");
		}
		if($eflg4 eq"$in{'mail'}"){&error2("你輸入的Email已被申請");}
		if($ename eq"$in{'name'}"){&error2("你輸入的角色名稱已被申請");}
		if($eid eq"$in{'id'}"){&error2("你輸入的帳號已被申請。");}
		
	}
	if($cn>10000){&error("ループ");}
	$cn++;
}
closedir(dirlist);

if($ATTESTATION){
	&mail_to;
}
	
unshift(@CHARA_DATA,"$id<>$pass<>$in{'name'}<>$os<>$in{'img'}<>$in{'sex'}<>$hp<>$hp<>$mp<>$mp<>$in{'ele'}<>$str<>$vit<>$int<>$fai<>$dex<>$agi<>$max<><>$gold<>$bank<>0<>0<>0<>0<>$cex<><>$in{'con_id'}<>$arm<>$pro<>$acc<>$tac<>$sta<>$pos<>$mes<>$host<>$date<>$date<>$class<>$total<>$kati<>0<><><>1<><><>$in{'mail'}<><>$pet<>\n");

open(OUT,">./logfile/chara/$in{'id'}.cgi") or &error2('建立失敗：角色檔案無法寫入。');
print OUT @CHARA_DATA;
close(OUT);
$mid="$id";
&kh_log("成為$con_name國的國民。",$con_name);
&maplog("<font color=999933>[新進]</font>歡迎<font color=333399>$in{'name'}</font>加入了「$con_name國」</font>。");

&header;

print <<"EOF";
<P align="center"><BR>
登錄完成</P>
<CENTER>
<TABLE border="0" width="415" height="67" bgcolor="#990099">
  <TBODY>
    <TR>
      <TD bgcolor="#660066" colspan="3" align="center"><FONT color="#ffffcc">登錄情報</FONT></TD>
    </TR>
    <TR>
      <TD bgcolor="#ffffcc">角色名稱</TD>
      <TD bgcolor="#ffffcc">$in{'name'}</TD>
    </TR><TR>
      <TD bgcolor="#ffffcc">帳號</TD>
      <TD bgcolor="#ffffcc">$id</TD>
    </TR>
    <TR>
      <TD bgcolor="#ffffcc">密碼</TD>
      <TD bgcolor="#ffffcc">$pass</TD>
    </TR>
    <TR>
      <TD bgcolor="#ffffcc">所屬國家</TD>
      <TD bgcolor="#ffffcc">$con_name</TD>
    </TR>
    <TR>
      <TD colspan="3" bgcolor="#ffcc99"><FONT color="#993399">帳號已新建完成。<BR>
      請記得你的帳號及密碼。<BR>
      </TD>
    </TR>
    <TR>
      <TD colspan="3" align=center bgcolor="#ffcc99">
      	<form action="./top.cgi" method="POST">
	<INPUT type=hidden name=id value=$in{'id'}>
	<INPUT type=hidden name=pass value=$in{'pass'}>
	<INPUT type=submit CLASS=FC value=進入遊戲></form>
      </TD>
    </TR>
  </TBODY>
</TABLE>
</CENTER>

EOF

&mainfooter;
exit;
