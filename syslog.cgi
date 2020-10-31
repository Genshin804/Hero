#! /usr/bin/perl
require './jcode.pl';
require './sub.cgi';
require './conf.cgi';
&decode;
&header;

$SNAME[0]="系統公告";
$SFILE[0]="maplog9";
$SNAME[1]="使用紀錄";
$SFILE[1]="maplog4";
$SNAME[2]="警告紀錄";
$SFILE[2]="maplog3";
$SNAME[3]="改名紀錄";
$SFILE[3]="maplog6";
$SNAME[4]="打寶紀錄";
$SFILE[4]="maplog7";
$SNAME[5]="傳送紀錄";
$SFILE[5]="maplog8";
$SNAME[6]="寵物轉生紀錄";
$SFILE[6]="maplog10";
$SNAME[7]="鐵匠注入奧義紀錄";
$SFILE[7]="maplogmix";
$SNAME[8]="任務紀錄";
$SFILE[8]="questlog";
$SNAME[9]="外掛紀錄";
$SFILE[9]="robotlog";
$logid=$in{'id'};
if($logid ne "1" && $logid ne "2" && $logid ne "3" && $logid ne "4" && $logid ne "5" && $logid ne "6" && $logid ne "7" && $logid ne "8" && $logid ne "9"){
	$logid="0";
}

open(IN,"./data/$SFILE[$logid].cgi");
@MA = <IN>;
close(IN);
foreach(@MA){
        $mapl.="<b><font color=$FCOLOR>●$MA[$m]</font></b><BR>";
        $m++;
}
for($i=0;$i<10;$i++){
	$mapmenu.="<a href=./syslog.cgi?id=$i>$SNAME[$i]</a>　";
}
print <<"EOF";
<CENTER>
<TABLE border="0" bgcolor="#660033" width="700" cellspacing="5" height="509">
  <TBODY>
        <TR>
                <TD colspan="2" bgcolor="#ffffcc" height="1" align="center">
$mapmenu
                </TD>
        </TR>
    <TR>
      <TD colspan="2" bgcolor="#ffffcc"><FONT style="font-size:15px" color="#666600"><$SNAME[$logid]><BR>$mapl</FONT><BR></TD>
    </TR>
  </TBODY>
</TABLE>
<BR>
</P>
</CENTER>

<hr>
EOF
&mainfooter;
exit;
