#!/usr/bin/perl

#################################################################
#   【免責事項】                                                #
#    このスクリプトはフリーソフトです。このスクリプトを使用した #
#    いかなる損害に対して作者は一切の責任を負いません。         #
#    また設置に関する質問はサポート掲示板にお願いいたします。   #
#    直接メールによる質問は一切お受けいたしておりません。       #
#################################################################

require './jcode.pl';
require './conf.cgi';
require './sub.cgi';

&decode;
	$adminid = "後端帳號";
	$adminpass = "後端密碼";
	$mode = "$in{'mode'}";
#20天未上線並未滿5000戰者
$del_day=20;
$del_total=5000;
if($mode eq 'MENTE') { &MENTE; }
elsif($mode eq 'DEL') { &DEL; }
elsif($mode eq 'INIT_DATA') { &INIT_DATA; }
elsif($mode eq 'INIT_DATA2') { &INIT_DATA2; }
elsif($mode eq 'WARN') { &WARN; }
elsif($mode eq 'PUBMSG') { &PUBMSG; }
elsif($mode eq 'LOGIN') { &LOGIN; }
elsif($mode eq 'MINDEL') { &MINDEL; }
elsif($mode eq 'MINDEL2') { &MINDEL2; }
elsif($mode eq 'SEARCHID') { &SEARCHID; }
elsif($mode eq 'SEARCHMNAME') { &SEARCHMNAME; }
elsif($mode eq 'SEARCHDFID') { &SEARCHDFID; }
else{&TOP;}


#_/_/_/_/_/_/_/_/_/#
#_/   MAIN画面   _/#
#_/_/_/_/_/_/_/_/_/#

sub TOP {

	if($in{'id'} ne "$adminid" || $in{'pass'} ne "$adminpass"){
	&error2("帳號或密碼錯誤 $num ");}


	&header;
	print <<"EOM";
<h2>管理介面</h2>
<CENTER>
<table width=80% cellspacing=1 border=0 bgcolor=aa0000><TBODY bgcolor=FFFFF8>
<TR><Th>
<form method="post" action="./admin.cgi">
<input type=hidden name=mode value=SEARCHID>
<input type=text name=mname size=15>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='查帳號'>
</form>
<form method="post" action="./admin.cgi">
<input type=hidden name=mode value=SEARCHMNAME>
<input type=text name=searchid size=15>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='查名稱'>
</form>
<form method="post" action="./admin.cgi">
<input type=hidden name=mode value=SEARCHDFID>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='查帳號與檔名不同'>
<br></form>
</Th><TD>
・查帳號。
</TD></TR>
<TR><Th>
<form method="post" action="admin.cgi">
<input type=hidden name=mode value=MENTE>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='帳號刪除'>
<br></form>
</Th><TD>
・刪除角色帳號。
</TD></TR>
<TR><Th>
<form method="post" action="admin.cgi">
<input type=hidden name=mode value=INIT_DATA>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=button value='所有資料初始化(太危險,防按錯停用)'>
<br></form>
</Th><TD>
・將所有的資料初始化(包括帳號)。
</TD></TD></TR>
<TR><Th>
<form method="post" action="admin.cgi">
<input type=hidden name=mode value=INIT_DATA2>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=button value='帳號以外資料初始化(暫鎖)'>
<br></form>
</Th><TD>
・將帳號以外的資料初始化。
</TD></TD></TR>

<TR><Th>
<form method="post" action="admin.cgi">
<input type=hidden name=mode value=MINDEL>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='閒置帳號刪除'>
<br></form>
</Th><TD>
・$del_day天未滿$del_total戰者刪除。
</TD></TD></TR>

<TR><Th>
<form method="post" action="admin.cgi">
<input type=hidden name=mode value=LOCK>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
(外掛帳號)<input type=text name=lockid>
<input type=submit value='外掛鎖檔'>
<br></form>
</Th><TD>
・參考logfile/verchk/檔案進行鎖檔。
</TD></TD></TR>

<TR><Th>
<form method="post" action="admin.cgi">
<input type=hidden name=mode value=WARN>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=text name=player>
<input type=submit value='警告'>
<br></form>
</Th><TD>
・輸入要警告的訊息。
</TD></TD></TR>

<TR><Th>
<form method="post" action="admin.cgi">
<input type=hidden name=mode value=PUBMSG>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=text name=pubmsg>
<input type=submit value='系統公告'>
<br></form>
</Th><TD>
・輸入要公告的訊息。
</TD></TD></TR>


<TR><Th>
<form method="post" action="admin.cgi">
<input type=hidden name=mode value=LOGIN>
ID:<input type=text size=15 name=id><BR>
PASS:<input type=password size=15 name=pass><BR>
<input type=hidden name=aid value="$in{id}">
<input type=hidden name=apass value="$in{pass}">
<input type=submit value='登入遊戲'>
<br></form>
</Th><TD>
・直接進入遊戲。
</TD></TD></TR>
</TBODY></TABLE>

<form method="post" action="index.cgi">
</select><input type=submit value='回到首頁'>
<br></form>

</CENTER>

EOM
	&mainfooter;
	exit;
}

#_/_/_/_/_/_/_/_/_/#
#_/  MENTE画面   _/#
#_/_/_/_/_/_/_/_/_/#

sub MENTE {

	if($in{'id'} ne "$adminid" || $in{'pass'} ne "$adminpass"){
	&ERR2("帳號或密碼錯誤 ");}

$dir="./logfile/chara";
opendir(dirlist,"$dir");
$i=0;
while($file = readdir(dirlist)){
	if($file =~ /\.cgi/i){
		$datames = "查詢：$dir/$file<br>\n";
		if(!open(page,"$dir/$file")){
			$datames .= "找不到檔案：$dir/$file。<br>\n";
			return 1;
		}
		@page = <page>;
		close(page);
		$list[$i]="$file";
		($eid,$epass,$ename,$eurl,$echara,$esex,$ehp,$emaxhp,$emp,$emaxmp,$eele,$estr,$evit,$eint,$efai,$edex,$eagi,$emax,$ecom,$egold,$ebank,$eex,$etotalex,$ejp,$eabp,$ecex,$eunit,$econ,$earm,$epro,$eacc,$etec,$esta,$epos,$emes,$ehost,$edate,$esyo,$eclass,$etotal,$ekati,$etype,$eoya,$esk,$eflg,$eflg2,$eflg3,$eflg4,$eflg5,$epet) = split(/<>/,$page[0]);

		if("$in{'serch'}" ne ""){
			if("$ename" =~ "$in{'serch'}"){
				$human_data[$i]="$ehost<>$ename<>$eid<>";
			}else{
				next;
			}
		}else{
			if($in{'no'} eq "2"){
				$human_data[$i]="$ename<>$ehost<>$eid<>";
			}elsif($in{'no'} eq "3"){
				$human_data[$i]="$eid<>$ehost<>$ename<>";
			}else{
				$human_data[$i]="$ename<>$ehost<>$eid<>";
			}
		}
		push(@newlist,"@page<br>");
		$i++;
	}
}
	closedir(dirlist);

	@human_data = sort @human_data;

$tt = time - (60 * 60 * 24 * 34);
($sec,$min,$hour,$mday,$mon,$year,$wday,$yday) = localtime($tt);
$year += 1900;
$mon++;
$ww = (Sun,Mon,Tue,Wed,Thu,Fri,Sat)[$wday];
$daytime = sprintf("%4d\/%02d\/%02d\/(%s) %02d:%02d:%02d", $year,$mon,$mday,$ww,$hour,$min,$sec);


	&header;
	print <<"EOM";
<font color="yellow">
<h2>帳號管理</h2>
<br>
・名稱請隨時更新。<br>
<form method="post" action="admin.cgi">
<input type=hidden name=mode value=DEL>輸入要刪除的帳號：
<input type=text name=fileno>(需加入.cgi)及密碼<input type=password name=mpass>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=hidden name=opt value="2">
<input type=submit value='刪除'>
<br></form>

<form method="post" action="admin.cgi">
<input type=hidden name=mode value=DEL>選擇要刪除的帳號：
<select name=fileno>
EOM
$i=0;$w_host="";
foreach(@human_data){
	if($in{'no'} eq "2"){
		($ename,$ehost,$eid) = split(/<>/);
	}elsif($in{'no'} eq "3"){
		($eid,$ehost,$ename) = split(/<>/);
	}else{
		($ename,$ehost,$eid) = split(/<>/);
	}
	print "<option value=$eid\.cgi>$eid $ename $ehost\n";
	if($in{'no'} eq "" || $in{'no'} eq "1"){
		if($w_host eq "$ehost"){
			$mess .= "$ename | $w_name<BR>\n";
		}
	}
	$w_host = "$ehost";
	$w_name = "$ename";
	$i++;
}
print <<"EOM";
</select><input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='刪除'>
<br></form>

２多重登錄者清單<p>
<font color=red>$mess</font>
<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='TOP'>
<br></form>

EOM

	&mainfooter;
	exit;
}

#_/_/_/_/_/_/_/_/_/#
#_/ ファイル削除 _/#
#_/_/_/_/_/_/_/_/_/#

sub DEL {

	if($in{'id'} ne "$adminid" || $in{'pass'} ne "$adminpass"){
		&error("帳號或密碼錯誤 $num ");
	}

	open(IN,"./logfile/chara/$in{'fileno'}") or &error('要刪除的角色己不存在。');
	@CN_DATA = <IN>;
	close(IN);
	($kid,$kpass,$kname) = split(/<>/,$CN_DATA[0]);
	if($in{'opt'} eq"2" && $kpass ne $in{'mpass'}){&error("密碼錯誤。");}
			$dir2="./logfile/chara";
			unlink("$dir2/$in{'fileno'}");
			$dir2="./logfile/item";
			unlink("$dir2/$in{'fileno'}");
			$dir2="./logfile/job";
			unlink("$dir2/$in{'fileno'}");
			$dir2="./logfile/ability";
			unlink("$dir2/$in{'fileno'}");
			$dir2="./logfile/history";
			unlink("$dir2/$in{'fileno'}");
                        $dir2="./logfile/storage";
                        unlink("$dir2/$in{'fileno'}");
                        $dir2="./logfile/ext";
                        unlink("$dir2/$in{'fileno'}");
                        $dir2="./logfile/act";
                        unlink("$dir2/$in{'fileno'}");
                        $dir2="./logfile/verchk";
                        unlink("$dir2/$in{'fileno'}");
                        $dir2="./logfile/fixext";
                        unlink("$dir2/$in{'fileno'}");
	#解除守備
        open(IN,"./data/def.cgi");
        @DEF = <IN>;
        close(IN);
        $hit=0;
        @NDEF=();
        foreach(@DEF){
                ($name,$id,$pos)=split(/<>/);
                if($id eq "$kid"){$hit=1;}
                else{push(@NDEF,"$_");}
        }
        if($hit){
	        open(OUT,">./data/def.cgi");
	        print OUT @NDEF;
	        close(OUT);
	}
	open(IN,"./data/maplog.cgi");
	@S_MOVE = <IN>;
	close(IN);
	&time_data;

	unshift(@S_MOVE,"<font color=red><B>\[刪除\]</B></font> <font color=red>$kname</font> 已被系統刪除。($mday日$hour時$min分)\n");
	splice(@S_MOVE,20);

	open(OUT,">./data/maplog.cgi") or &error2('檔案開啟錯誤admin.cgi(263)。');
	print OUT @S_MOVE;
	close(OUT);
        open (OUT, "> ./data/maplogtime.cgi");
        print OUT $tt;
        close (OUT);

	&header;
	print <<"EOM";
<center><h2><font color=red>$kname已被刪除。</font></h2><hr size=0>
<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='返回'>
<br></form>
EOM

	&mainfooter;
	exit;
}

#_/_/_/_/_/_/_/_/_/#
#_/   編集画面   _/#
#_/_/_/_/_/_/_/_/_/#

sub INIT_DATA {

	if($in{'id'} ne "$adminid" || $in{'pass'} ne "$adminpass"){
		&error2("帳號或密碼錯誤 $num ");
	}
	require "reset.cgi";
	&RESET_MODE;
	
	&header;
	print <<"EOM";
<h2><font color=red>所以資料初使化完成。</h2></font>
<br>
<br>
<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='返回'>
</form>
<br>
EOM

	&mainfooter;
	exit;
}


#_/_/_/_/_/_/_/_/_/#
#_/   編集画面   _/#
#_/_/_/_/_/_/_/_/_/#

sub INIT_DATA2 {

	if($in{'id'} ne "$adminid" || $in{'pass'} ne "$adminpass"){
		&error2("帳號或密碼錯誤 $num ");
	}
	require "reset.cgi";
	&RESET_MODE2;
	
	&header;
	print <<"EOM";
<h2><font color=red>帳號以外資料初始化完成。</h2></font>
<br>
<br>
<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='返回'>
</form>
<br>
EOM

	&mainfooter;
	exit;
}

#_/_/_/_/_/_/_/_/_/#
#_/   編集画面   _/#
#_/_/_/_/_/_/_/_/_/#

sub WARN {

	if($in{'id'} ne "$adminid" || $in{'pass'} ne "$adminpass"){
		&error2("帳號或密碼錯誤 $num ");
	}
	&maplog("<font color=red>[系統警告]</font>己對$in{'player'}發出警告。");
        open (OUT, "> ./data/maplogtime.cgi");
        print OUT $tt;
        close (OUT);

	&header;
	print <<"EOM";
<h2><font color=red>警告訊息發送。</h2></font>
<br>
<br>
<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='返回'>
</form>
<br>
EOM

	&mainfooter;
	exit;
}

sub PUBMSG {

        if($in{'id'} ne "$adminid" || $in{'pass'} ne "$adminpass"){
                &error2("帳號或密碼錯誤 $num ");
        }
        &maplog("<font color=red><b>[系統公告]</b>$in{'pubmsg'}。</font>");
        &maplog9("<font color=darkgreen><b>[系統公告]</b></font><font color=blue>$in{'pubmsg'}。</font>");
        open (OUT, "> ./data/maplogtime.cgi");
        print OUT $tt;
        close (OUT);

        &header;
        print <<"EOM";
<h2><font color=red>公告訊息發送。</h2></font>
<br>
<br>
<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='返回'>
</form>
<br>
EOM

        &mainfooter;
        exit;
}


#_/_/_/_/_/_/_/_/_/#
#_/   編集画面   _/#
#_/_/_/_/_/_/_/_/_/#

sub LOGIN {

	if($in{'aid'} ne "$adminid" || $in{'apass'} ne "$adminpass"){
		&error2("帳號或密碼錯誤 $num ");
	}
	$login=1;
	
	&chara_open;
	&chara_input;
	&header;
	print <<"EOM";
<h2><font color=red>認證完成。</h2></font>
<br>
<br>
<form method="post" action="top.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='進入'>
</form>
<br>
EOM

	&mainfooter;
	exit;
}

#_/_/_/_/_/_/_/_/_/#
#_/ 放置者一覧 _/#
#_/_/_/_/_/_/_/_/_/#

sub MINDEL {

	if($in{'id'} ne "$adminid" || $in{'pass'} ne "$adminpass"){
		&error("帳號或密碼錯誤 $num ");
	}


	# MAIN DATA
	$dir="./logfile/chara";
	opendir(dirlist,"$dir");
$delcount=0;
$del_day2=$del_day*60*60*24;
	$date = time();
	while($file = readdir(dirlist)){
		if($file =~ /\.cgi/i){
			$datames = "查詢：$dir/$file<br>\n";
			if(!open(page,"$dir/$file")){
				$datames .= "找不到檔案：$dir/$file。<br>\n";
				return 1;
			}
			@page = <page>;
			close(page);
			$list[$i]="$file";
			($eid,$epass,$ename,$eurl,$echara,$esex,$ehp,$emaxhp,$emp,$emaxmp,$eele,$estr,$evit,$eint,$efai,$edex,$eagi,$emax,$ecom,$egold,$ebank,$eex,$etotalex,$ejp,$eabp,$ecex,$eunit,$econ,$earm,$epro,$eacc,$etec,$esta,$epos,$emes,$ehost,$edate,$esyo,$eclass,$etotal,$ekati,$etype,$eoya,$esk,$eflg,$eflg2,$eflg3,$eflg4,$eflg5,$epet) = split(/<>/,$page[0]);
$date2=$date-$edate;
			if($etotal<$del_day && $date2>$del_day2){
				$mess.="$ename<BR>";
				$delcount++;
			}
		}
	}
	closedir(dirlist);

	&header;
	print <<"EOM";
<center><h2><font color=red>$del_day天未上線未滿$del_total戰者刪除。<BR></font></h2><hr size=0>
<font color=white>
(共$delcount名)
$mess
</font>
<form method="post" action="admin.cgi">
<input type=hidden name=mode value=MINDEL2>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='刪除'>
<br></form>

<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='返回'>
<br></form>
EOM

	&mainfooter;
	exit;
}

#_/_/_/_/_/_/_/_/_/#
#_/查詢角色帳號  _/#
#_/_/_/_/_/_/_/_/_/#

sub SEARCHID {
        if($in{'id'} ne "$adminid" || $in{'pass'} ne "$adminpass"){
                &error("帳號或密碼錯誤 $num ");
        }
        $dir="./logfile/chara";
        opendir(dirlist,"$dir");
        while($file = readdir(dirlist)){
                if($file =~ /\.cgi/i){
                        $datames = "查詢：$dir/$file<br>\n";
                        if(!open(page,"$dir/$file")){
                                $datames .= "找不到檔案：$dir/$file。<br>\n";
                                return 1;
                        }
                        @page = <page>;
                        close(page);
                        $list[$i]="$file";
                        ($eid,$epass,$ename,$eurl,$echara,$esex,$ehp,$emaxhp,$emp,$emaxmp,$eele,$estr,$evit,$eint,$efai,$edex,$eagi,$emax,$ecom,$egold,$ebank,$eex,$etotalex,$ejp,$eabp,$ecex,$eunit,$econ,$earm,$epro,$eacc,$etec,$esta,$epos,$emes,$ehost,$edate,$esyo,$eclass,$etotal,$ekati,$etype,$eoya,$esk,$eflg,$eflg2,$eflg3,$eflg4,$eflg5,$epet) = split(/<>/,$page[0]);
			if($ename eq"$in{'mname'}"){
				$mid=$eid;
				$mpass=$epass;
				last;
			}
		}
	}
        &header;
        print <<"EOM";
<center><h2><font color=red>查詢帳號結果。<BR><font color="yellow">$mid</font><BR><font color="yellow">$mpass</font></h2><hr size=0>
<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='返回'>
<br></form>
EOM

	&mainfooter;
	exit;
}

#_/_/_/_/_/_/_/_/_/#
#_/查詢角色名稱  _/#
#_/_/_/_/_/_/_/_/_/#

sub SEARCHMNAME {
        if($in{'id'} ne "$adminid" || $in{'pass'} ne "$adminpass"){
                &error("帳號或密碼錯誤 $num ");
        }
        if($in{'searchid'} ne""){
                open(IN,"./logfile/chara/$in{'searchid'}.cgi") or &error('此帳號尚未創立。');
        }else{
                if(in{'searchid'} eq ""){&error2("帳號有誤");}
                open(IN,"./logfile/chara/in{'searchid'}.cgi") or &error('此帳號尚未創立。');
        }
        @CH_DATA = <IN>;
        close(IN);
        ($mid,$mpass,$mname,$murl,$mchara,$msex,$mhp,$mmaxhp,$mmp,$mmaxmp,$mele,$mstr,$mvit,$mint,$mfai,$mdex,$magi,$mmax,$mcom,$mgold,$mbank,$mex,$mtotalex,$mjp,$mabp,$mcex,$munit,$mcon,$marm,$mpro,$macc,$mtec,$msta,$mpos,$mmes,$mhost,$mdate,$mdate2,$mclass,$mtotal,$mkati,$mtype,$moya,$msk,$mflg,$mflg2,$mflg3,$mflg4,$mflg5,$mpet) = split(/<>/,$CH_DATA[0]);

        &header;
        print <<"EOM";
<center><h2><font color=red>查詢帳號結果。<BR><font color="yellow">$mid</font><BR><font color="yellow">$mname</font><BR><font color="yellow">$mpass</font></h2><hr size=0>
<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='返回'>
<br></form>
EOM

        &mainfooter;
        exit;
}

#_/_/_/_/_/_/_/_/_/#
#_/ 放置者削除 _/#
#_/_/_/_/_/_/_/_/_/#

sub MINDEL2 {

	if($in{'id'} ne "$adminid" || $in{'pass'} ne "$adminpass"){
		&error("帳號或密碼錯誤 $num ");
	}

	$date = time();
$delcount=0;
$del_day2=$del_day*60*60*24;
	# MAIN DATA
	$dir="./logfile/chara";
	opendir(dirlist,"$dir");
	while($file = readdir(dirlist)){
		if($file =~ /\.cgi/i){
			$datames = "查詢：$dir/$file<br>\n";
			if(!open(page,"$dir/$file")){
				$datames .= "找不到檔案：$dir/$file。<br>\n";
				return 1;
			}
			@page = <page>;
			close(page);
			$list[$i]="$file";
			($eid,$epass,$ename,$eurl,$echara,$esex,$ehp,$emaxhp,$emp,$emaxmp,$eele,$estr,$evit,$eint,$efai,$edex,$eagi,$emax,$ecom,$egold,$ebank,$eex,$etotalex,$ejp,$eabp,$ecex,$eunit,$econ,$earm,$epro,$eacc,$etec,$esta,$epos,$emes,$ehost,$edate,$esyo,$eclass,$etotal,$ekati,$etype,$eoya,$esk,$eflg,$eflg2,$eflg3,$eflg4,$eflg5,$epet) = split(/<>/,$page[0]);
$date2=$date-$edate;
                        if($etotal<$del_day && $date2>$del_day2){

#			if($etotal<10 && $date>$edate+604800){
				$dir2="./logfile/chara";
				unlink("$dir2/$eid.cgi");
				$dir2="./logfile/item";
				unlink("$dir2/$eid.cgi");
                                $dir2="./logfile/storage";
                                unlink("$dir2/$eid.cgi");
				$dir2="./logfile/job";
				unlink("$dir2/$eid.cgi");
				$dir2="./logfile/ability";
				unlink("$dir2/$eid.cgi");
				$dir2="./logfile/history";
				unlink("$dir2/$eid.cgi");
				$dir2="./logfile/out";
				unlink("$dir2/$eid.cgi");
				$dir2="./logfile/mes";
				unlink("$dir2/$eid.cgi");
				$dir2="./logfile/prof";
				unlink("$dir2/$eid.cgi");
                                $dir2="./logfile/fixext";
                                unlink("$dir2/$eid.cgi");
				$mess.="$ename<BR>";
				$count++;
			}
		}
	}
	closedir(dirlist);
	&maplog("<font color=red><b>[系統公告]</b></font>$del_day天內未上線並未滿$del_total戰者($count名)帳號刪除。</font>");	
	&maplog9("<font color=darkgreen><b>[系統公告]</b></font><font color=blue>$del_day天內未上線並未滿$del_total戰者($count名)帳號刪除。</font>");

	&header;
	print <<"EOM";
<center><h2><font color=red>本次刪除清單如下帳號。<BR>$mess</font></h2><hr size=0>
<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='返回'>
<br></form>
EOM

	&mainfooter;
	exit;
}

##查檔名跟id不一樣的
sub SEARCHDFID {
        if($in{'id'} ne "$adminid" || $in{'pass'} ne "$adminpass"){
                &error("帳號或密碼錯誤 $num ");
        }
        $dir="./logfile/chara";
        opendir(dirlist,"$dir");
        while($file = readdir(dirlist)){
                if($file =~ /\.cgi/i){
                        $datames = "查詢：$dir/$file<br>\n";
                        if(!open(page,"$dir/$file")){
                                $datames .= "找不到檔案：$dir/$file。<br>\n";
                                return 1;
                        }
                        @page = <page>;
                        close(page);
                        $list[$i]="$file";
                        ($eid,$epass,$ename,$eurl,$echara,$esex,$ehp,$emaxhp,$emp,$emaxmp,$eele,$estr,$evit,$eint,$efai,$edex,$eagi,$emax,$ecom,$egold,$ebank,$eex,$etotalex,$ejp,$eabp,$ecex,$eunit,$econ,$earm,$epro,$eacc,$etec,$esta,$epos,$emes,$ehost,$edate,$esyo,$eclass,$etotal,$ekati,$etype,$eoya,$esk,$eflg,$eflg2,$eflg3,$eflg4,$eflg5,$epet) = split(/<>/,$page[0]);
                        if($file ne"$eid".".cgi"){
				$dflist.="<font size=3><b>$file</b></font><BR>";
				$dflist.="<font size=2>$page[0]<BR></font>";
                        }
                }
        }
        &header;
        print <<"EOM";
<center><h2><font color=red>查詢帳號與檔名不同結果。<BR>
<p align="left"><font color="yellow">$dflist</p>
<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='返回'>
<br></form>
EOM

        &mainfooter;
        exit;
}
        
