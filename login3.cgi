#! /usr/bin/perl
require './jcode.pl';
require './sub.cgi';
require './conf.cgi';
&decode;


open(IN,"./data/apo.cgi");
@apo = <IN>;
close(IN);
&host_name;
$timer = time();@newapo=();
open(IN,"./logfile/chara/$in{'id'}.cgi") or &error2('請輸入正確的帳號及匿稱。');
@CH_DATA = <IN>;
        close(IN);
        ($mid,$mpass,$mname,$murl,$mchara,$msex,$mhp,$mmaxhp,$mmp,$mmaxmp,$mele,$mstr,$mvit,$mint,$mfai,$mdex,$magi,$mmax,$mcom,$mgold,$mbank,$mex,$mtotalex,$mjp,$mabp,$mcex,$munit,$mcon,$marm,$mpro,$macc,$mtec,$msta,$mpos,$mmes,$mhost,$mdate,$mdate2,$mclass,$mtotal,$mkati,$mtype,$moya,$msk,$mflg,$mflg2,$mflg3,$mflg4,$mflg5,$mpet) = split(/<>/,$CH_DATA[0]);
if($mname ne $in{'name'}){&error2('請輸入正確的帳號及匿稱。');}
foreach(@apo) {
	($gname,$gid,$gtime)=split(/<>/);
	if($timer>$gtime+900){next;}
	elsif($in{'id'} eq $gid){
		&error2("已在預約名單中。");
	}
	else{
		push(@newapo,"$gname<>$gid<>$gtime<>\n");
	}
}
	push(@newapo,"$in{'name'}<>$in{'id'}<>$timer<>\n");

open(OUT,">./data/apo.cgi") or &error('檔案無法存取(login3.cgi)26。');
print OUT @newapo;
close(OUT);

&header;

print <<"EOF";
<BR>
<BR>
<CENTER>
<form action="index.cgi" method="POST">
<TABLE border="0" width="200" CLASS=FC>
  <TBODY>
    <TR>
      <TD bgcolor=$FCOLOR colspan=2 align=center><font size=3 color=$FCOLOR2>預約完成</font></TD>
    </TR>
    <TR>
      <TD colspan="2" align=center>
	<input type=hidden name=id value=$mid>
    	<input type=submit CLASS=FC value=TOPへ></TD>
    </TR>
  </TBODY>
</TABLE>
</CENTER>
</form>
EOF
&mainfooter;
exit;
