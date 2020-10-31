#####################
## キャラ読込/書込 ##
#####################

sub chara_open{
        if($open_chara_id ne""){
                open(IN,"./logfile/chara/$open_chara_id.cgi") or &error2('此帳號尚未創立。');
        }else{
                if($in{'id'} eq ""){&error2("帳號有誤");}
                open(IN,"./logfile/chara/$in{'id'}.cgi") or &error2('此帳號尚未創立。');
        }
	@CH_DATA = <IN>;
	close(IN);
	($mid,$mpass,$mname,$murl,$mchara,$msex,$mhp,$mmaxhp,$mmp,$mmaxmp,$mele,$mstr,$mvit,$mint,$mfai,$mdex,$magi,$mmax,$mcom,$mgold,$mbank,$mex,$mtotalex,$mjp,$mabp,$mcex,$munit,$mcon,$marm,$mpro,$macc,$mtec,$msta,$mpos,$mmes,$mhost,$mdate,$mdate2,$mclass,$mtotal,$mkati,$mtype,$moya,$msk,$mflg,$mflg2,$mflg3,$mflg4,$mflg5,$mpet) = split(/<>/,$CH_DATA[0]);
	#Ajax角色情報
	$ajax_chara_data="CHARA<>$mname<>$mchara<>$mhp<>$mmaxhp<>$mmp<>$mmaxmp<>$ELE[$mele]<>$mstr<>$mvit<>$mint<>$mfai<>$mdex<>$magi<>$mmax<>$mcom<>$mgold<>$mbank<>$mex<>$mtotalex<>$mjp<>$mabp<>$mcex<>$munit<>$mcon<>$marm<>$mpro<>$macc<>$mtec<>$msta<>$mpos<>$mmes<>$mhost<>$mdate<>$mdate2<>$JOB[$mclass]<>$mtotal<>$mkati<>$mtype<>$moya<>$msk<>$mflg<>$mflg2<>$mflg3<>$mflg4<>$mflg5<>$mpet<>$TYPE[$mtype]<>\n";
	#資金換算
	$smgold=int($mgold/10000);
	if ($smgold>9999) {
	        $smgold=int($smgold/10000)."億".($smgold%10000)."萬".($mgold%10000);
	}elsif($mgold<10000){
	        $smgold="$mgold Gold";
	}else{
	        $smgold.="萬".($mgold%10000);;
	}
	$smbank=int($mbank/10000);
	if ($smbank>9999) {
	        $smbank=int($smbank/10000)."億".($smbank%10000)."萬".($mbank%10000);
	}elsif($mbank<10000){
	        $smbank="$mbank Gold";
	}else{
	        $smbank.="萬".($mbank%10000);;
	}

	$date = time();
	$IDLETIME+=int($mtotal/200);
	if($IDLETIME>600){
		$IDLETIME=600;
	}
	if(!$login && $date>$mdate+$IDLETIME && $mid ne $GMID){
		&ext_open;
		if($member_point eq""){
			&error2("你已有一段時間($IDLETIME秒)未動作，<a href='./login.cgi'>請重新登入</a>。");
		}
        }

	$mlv = int($mex/100)+1;
	($mjp[0],$mjp[1],$mjp[2],$mjp[3],$mjp[4],$mjp[5]) = split(/,/,$mjp);
	($mmaxstr,$mmaxvit,$mmaxint,$mmaxmen,$mmaxdex,$mmaxagi,$mmaxlv) = split(/,/,$mmax);
        if($open_chara_id ne""){
                if($open_chara_id ne "$mid"){&error2("角色檔案出錯，請確認您輸入的帳號密碼正確，如果一樣出現此訊息，請申請新帳號，留訊息給(GM)老頭兒，「我的角色帳號xxx，於x月x日無法登入」，GM看到此訊息將會進行處理，處理完後請刪除此分身帳號。");}
        }else{
                if($in{'id'} ne "$mid" or $in{'pass'} ne "$mpass"){&error2("角色檔案出錯，請確認您輸入的帳號密碼正確，如果一樣出現此訊息，請申請新>帳號，留訊息給(GM)老頭兒，「我的角色帳號xxx，於x月x日無法登入」，GM看到此訊息將會進行處理，處理完後請刪除此分身帳號。");}
        }
	$SP_LOG=0;
	if($LOG_ID[0] ne"" && $in{'id'} ne""){
		foreach(@LOG_ID){
			if($_ eq $in{'id'}){
				$SP_LOG=1;
				last;
			}
		}
	}
}

sub chara_input {
	&host_name;
	$date = time();
	@N_DATA=();
	$mjp = "$mjp[0],$mjp[1],$mjp[2],$mjp[3],$mjp[4],$mjp[5]";
	if($mhp>$mmaxhp){$mhp=$mmaxhp;}
        $mstr=int($mstr);
        $mvit=int($mvit);
        $mint=int($mint);
        $mfai=int($mfai);
        $mdex=int($mdex);
        $magi=int($magi);
	unshift(@N_DATA,"$mid<>$mpass<>$mname<>$murl<>$mchara<>$msex<>$mhp<>$mmaxhp<>$mmp<>$mmaxmp<>$mele<>$mstr<>$mvit<>$mint<>$mfai<>$mdex<>$magi<>$mmax<>$mcom<>$mgold<>$mbank<>$mex<>$mtotalex<>$mjp<>$mabp<>$mcex<>$munit<>$mcon<>$marm<>$mpro<>$macc<>$mtec<>$msta<>$mpos<>$mmes<>$host<>$date<>$mdate2<>$mclass<>$mtotal<>$mkati<>$mtype<>$moya<>$msk<>$mflg<>$mflg2<>$mflg3<>$mflg4<><>$mpet<><>\n");
	open(OUT,">./logfile/chara/$in{'id'}.cgi") or &error('角色資料有誤。');
	print OUT @N_DATA;
	close(OUT);
}

sub enemy_open{
	open(IN,"./logfile/chara/$enemy_id.cgi");
	@E_DATA = <IN>;
	close(IN);
	($eid,$epass,$ename,$eurl,$echara,$esex,$ehp,$emaxhp,$emp,$emaxmp,$eele,$estr,$evit,$eint,$efai,$edex,$eagi,$emax,$ecom,$egold,$ebank,$eex,$etotalex,$ejp,$eabp,$ecex,$eunit,$econ,$earm,$epro,$eacc,$etec,$esta,$epos,$emes,$ehost,$edate,$esyo,$eclass,$etotal,$ekati,$etype,$eoya,$esk,$eflg,$eflg2,$eflg3,$eflg4,$eflg5,$epet) = split(/<>/,$E_DATA[0]);
	$elv = int($eex/100)+1;
	if($enemy_id ne "$eid"){&error("帳號不正確。$eid");}
}

sub enemy_input {
	$date = time();
	@NE_DATA=();
	if($ename){
		if($ehp>$emaxhp){$ehp=$emaxhp;}
		unshift(@NE_DATA,"$eid<>$epass<>$ename<>$eurl<>$echara<>$esex<>$ehp<>$emaxhp<>$emp<>$emaxmp<>$eele<>$estr<>$evit<>$eint<>$efai<>$edex<>$eagi<>$emax<>$ecom<>$egold<>$ebank<>$eex<>$etotalex<>$ejp<>$eabp<>$ecex<>$eunit<>$econ<>$earm<>$epro<>$eacc<>$etec<>$esta<>$epos<>$emes<>$ehost<>$edate<>$edate2<>$eclass<>$etotal<>$ekati<>$etype<>$eoya<>$esk<>$eflg<>$eflg2<>$eflg3<>$eflg4<><>$epet<><>\n");
		open(OUT,">./logfile/chara/$enemy_id.cgi") or &error('帳號存檔失敗sub.cgi(44)。');
		print OUT @NE_DATA;
		close(OUT);
	}
}
#################
##　　ログ     ##
#################
#出来事
sub maplog{
	&time_data;
	open(IN,"./data/maplog.cgi") or error2("檔案開啟有誤sub.cgi(55)");
	@data = <IN>;
	close(IN);
	unshift(@data, "$_[0]($daytime)\n");
	splice(@data,10);
	open (OUT, "> ./data/maplog.cgi");
	print OUT @data;
	close (OUT);
	open (OUT, "> ./data/maplogtime.cgi");
        print OUT $tt;
        close (OUT);
}
sub questlog{
        &time_data;
        open(IN,"./data/questlog.cgi") or error2("檔案開啟有誤sub.cgi(55)");
        @data = <IN>;
        close(IN);
        unshift(@data, "$_[0]($daytime)\n");
        splice(@data,50);
        open (OUT, "> ./data/questlog.cgi");
        print OUT @data;
        close (OUT);
        open (OUT, "> ./data/maplogtime.cgi");
        print OUT $tt;
        close (OUT);
}

#歴史
sub maplog2{
	&time_data;
	open(IN,"./data/maplog2.cgi") or error2("檔案開啟有誤sub.cgi(67)");
	@data2 = <IN>;
	close(IN);
	unshift(@data2, "【$year年$mon月$mday日】$_[0]\n");
	splice(@data2,50);
	open (OUT, "> ./data/maplog2.cgi");
	print OUT @data2;
	close (OUT);
}
#警告
sub maplog3{
	&time_data;
	open(IN,"./data/maplog3.cgi") or error2("檔案開啟有誤sub.cgi(79)");
	@data = <IN>;
	close(IN);
	unshift(@data, "$_[0]($daytime)\n");
	splice(@data,30);
	open (OUT, "> ./data/maplog3.cgi");
	print OUT @data;
	close (OUT);
}
#寶物使用ログ
sub maplog4{
	&time_data;
	open(IN,"./data/maplog4.cgi") or error2("檔案開啟有誤sub.cgi(65)");
	@data = <IN>;
	close(IN);
	unshift(@data, "$_[0]($daytime)\n");
	splice(@data,50);
	open (OUT, "> ./data/maplog4.cgi");
	print OUT @data;
	close (OUT);
}
#戰鬥ログ
sub maplog5{
	&time_data;
	open(IN,"./data/maplog5.cgi") or error2("檔案開啟有誤sub.cgi(103)");
	@data5 = <IN>;
	close(IN);
	unshift(@data5, "$_[0]($daytime)\n");
	splice(@data5,10);
	open (OUT, "> ./data/maplog5.cgi");
	print OUT @data5;
	close (OUT);
        open (OUT, "> ./data/maplogtime.cgi");
        print OUT $tt;
        close (OUT);
}
#改名ログ
sub maplog6{
	&time_data;
	open(IN,"./data/maplog6.cgi") or error2("檔案開啟有誤sub.cgi(115)");
	@data6 = <IN>;
	close(IN);
	unshift(@data6, "$_[0]($daytime)\n");
	splice(@data6,30);
	open (OUT, "> ./data/maplog6.cgi");
	print OUT @data6;
	close (OUT);
}
#發見ログ
sub maplog7{
	&time_data;
	open(IN,"./data/maplog7.cgi") or error2("檔案開啟有誤sub.cgi(127)");
	@data7 = <IN>;
	close(IN);
	unshift(@data7, "$_[0]($daytime)\n");
	splice(@data7,30);
	open (OUT, "> ./data/maplog7.cgi");
	print OUT @data7;
	close (OUT);
}
#傳送紀錄
sub maplog8{
        &time_data;
        open(IN,"./data/maplog8.cgi") or error2("檔案開啟有誤sub.cgi(127)");
        @data8 = <IN>;
        close(IN);
        unshift(@data8, "$_[0]($daytime)\n");
        splice(@data8,30);
        open (OUT, "> ./data/maplog8.cgi");
        print OUT @data8;
        close (OUT);
}

#系統公告
sub maplog9{
        &time_data;
        open(IN,"./data/maplog9.cgi") or error2("檔案開啟有誤sub.cgi(133)");
        @data9 = <IN>;
        close(IN);
        unshift(@data9, "$_[0]($daytime)\n");
        splice(@data9,30);
        open (OUT, "> ./data/maplog9.cgi");
        print OUT @data9;
        close (OUT);
}

#寵物轉生紀錄
sub maplog10{
        &time_data;
        open(IN,"./data/maplog10.cgi") or error2("檔案開啟有誤sub.cgi(133)");
        @data10 = <IN>;
        close(IN);
        unshift(@data10, "$_[0]($daytime)\n");
        splice(@data10,30);
        open (OUT, "> ./data/maplog10.cgi");
        print OUT @data10;
        close (OUT);
}
#鐵匠奧義注入紀錄
sub maplogmix{
        &time_data;
        open(IN,"./data/maplogmix.cgi") or error2("檔案開啟有誤sub.cgi(133)");
        @datamix = <IN>;
        close(IN);
        unshift(@datamix, "$_[0]($daytime)\n");
        splice(@datamix,30);
        open (OUT, "> ./data/maplogmix.cgi");
        print OUT @datamix;
        close (OUT);
}


#國庫紀錄
sub maplog_constorage{
        &time_data;
        open(IN,"./logfile/constorage/$mcon"."_mes.cgi");
        @datacstorage = <IN>;
        close(IN);
        unshift(@datacstorage, "$_[0]($daytime)\n");
        splice(@datacstorage,50);
        open (OUT, "> ./logfile/constorage/$mcon"."_mes.cgi");
        print OUT @datacstorage;
        close (OUT);
}

sub kh_log{
	&time_data;
	open(IN,"./logfile/history/$mid.cgi");
	@data = <IN>;
	close(IN);
	unshift(@data, "$_[0]<>$_[1]<>$mon月$mday日\n");
	splice(@data,6);
	open (OUT, "> ./logfile/history/$mid.cgi");
	print OUT @data;
	close (OUT);
}
sub eh_log{
	&time_data;
	open(IN,"./logfile/history/$eid.cgi");
	@data = <IN>;
	close(IN);
	unshift(@data, "$_[0]<>$_[1]<>$mon月$mday日\n");
	splice(@data,6);
	open (OUT, "> ./logfile/history/$eid.cgi");
	print OUT @data;
	close (OUT);
}
sub verchklog{
        &time_data;
        open(IN,"./logfile/verchk/$in{'id'}.cgi");
        @data = <IN>;
        close(IN);
	unshift(@data, "$_[0],($daytime$sec)\n");
        #splice(@data,10);
        open (OUT, "> ./logfile/verchk/$in{'id'}.cgi");
        print OUT @data;
        close (OUT);
}

#################
##　　裝備     ##
#################
sub equip_open{
	($marmno,$marmname,$marmval,$marmdmg,$marmwei,$marmele,$marmhit,$marmcl,$marmsta,$marmtype,$marmflg) = split(/,/,$marm);
	($mprono,$mproname,$mproval,$mprodmg,$mprowei,$mproele,$mprohit,$mprocl,$mprosta,$mprotype,$mproflg) = split(/,/,$mpro);
	($maccno,$maccname,$maccval,$maccdmg,$maccwei,$maccele,$macchit,$macccl,$maccsta,$macctype,$maccflg) = split(/,/,$macc);
	($mpetcno,$mpetname,$mpetdmg,$mpetdef,$mpetspeed,$mpetele,$mpetlv,$mpetcl,$mpetsta,$mpettype,$mpetflg) = split(/,/,$mpet);
	($msk[0],$msk[1]) = split(/,/,$msk);
        ($tmp_arm_sk[0],$tmp_arm_sk[1]) = split(/:/,$marmsta);
        ($tmp_pro_sk[0],$tmp_pro_sk[1]) = split(/:/,$mprosta);
        ($tmp_acc_sk[0],$tmp_acc_sk[1]) = split(/:/,$maccsta);
        ($tmp_pet_sk[0],$tmp_pet_sk[1]) = split(/:/,$mpetsta);
#修正bug用
if ($mprodmg>2000){
        if($mproele eq"1"){
        	$mprodmg=450;
        	$mprowei=0;
        }elsif($mproele eq"2"){
        	$mprodmg=700;
        	$mprowei=50;
        }elsif($mproele eq"3"){
        	$mprodmg=450;
        	$mprowei=-50;
        }elsif($mproele eq"4"){
        	$mprodmg=550;
        	$mprowei=0;
        }elsif($mproele eq"5"){
        	$mprodmg=600;
        	$mprowei=30;
        }elsif($mproele eq"6"){
        	$mprodmg=600;
        	$mprowei=50;
        }elsif($mproele eq"7"){
        	$mprodmg=500;
        	$mprowei=0;
        }else{
        	$mprodmg=300;
        	$mprowei=50;
        }
	$mpro="$mprono,$mproname,$mproval,$mprodmg,$mprowei,$mproele,$mprohit,$mprocl,$mprosta,$mprotype,$mproflg";
}
if ($marmdmg>2000){
        if($marmele eq"1"){
        	$marmdmg=700;
        	$marmwei=50;
        }elsif($marmele eq"2"){
        	$marmdmg=450;
        	$marmwei=0;
        }elsif($marmele eq"3"){
        	$marmdmg=450;
        	$marmwei=-50;
        }elsif($marmele eq"4"){
        	$marmdmg=550;
        	$marmwei=0;
        }elsif($marmele eq"5"){
        	$marmdmg=600;
        	$marmwei=30;
        }elsif($marmele eq"6"){
        	$marmdmg=500;
        	$marmwei=0;
        }elsif($marmele eq"7"){
        	$marmdmg=600;
        	$marmwei=50;
        }else{
        	$marmdmg=300;
        	$marmwei=50;
        }
	$marm="$marmno,$marmname,$marmval,$marmdmg,$marmwei,$marmele,$marmhit,$marmcl,$marmsta,$marmtype,$marmflg";
}
if ($maccdmg>300){
    $maccdmg=100;
    $maccwei=-50;
    $macc="$maccno,$maccname,$maccval,$maccdmg,$maccwei,$maccele,$macchit,$macccl,$maccsta,$macctype,$maccflg";
}

#修正bug結束
	if($msk[0] eq "62" || $msk[1] eq "62"){$eleplus = 0.2;}
	elsif($tmp_arm_sk[0] eq "62" || $tmp_arm_sk[1] eq "62"){$eleplus = 0.2;}
	elsif($tmp_pro_sk[0] eq "62" || $tmp_pro_sk[1] eq "62"){$eleplus = 0.2;}
	elsif($tmp_acc_sk[0] eq "62" || $tmp_acc_sk[1] eq "62"){$eleplus = 0.2;}
	elsif($tmp_pet_sk[0] eq "62" || $tmp_pet_sk[1] eq "62"){$eleplus = 0.2;}
	$petname2="";
	if ($mpet eq""){
		$mpetdmg=0;
		$mpetdef=0;
		$mpetspeed=0;
	}else{
                $petname2="<font color=blue>+$mpetname.lv$mpetlv</font>";
	}
	if($mele eq "$marmele" && $marmele ne "0"){
		if($marmno eq"mix"){
			$marmdmg = int($marmdmg*(1.3 + $eleplus));
		}else{
			$marmdmg = int($marmdmg*(1.2 + $eleplus));
		}
	}
	if($mele eq "$mproele" && $mproele ne "0"){
		if($mprono eq"mix"){
			$mprodmg = int($mprodmg*(1.3 + $eleplus));
		}else{
			$mprodmg = int($mprodmg*(1.2 + $eleplus));
		}
	}
	if($mele eq "$maccele" && $maccele ne "0"){$maccdmg = int($maccdmg*(1.5 + $eleplus));}
	if($mele eq "$mpetele" && $mpetele ne "0"){
		$mpetdmg = int($mpetdmg*(1.2 + $eleplus));
		$mpetdef = int($mpetdef*(1.2 + $eleplus));
		$mpetspeed = int($mpetspeed*(1.2 + $eleplus));
	}
	if($ARM[$mclass] eq "$marmtype"){$marmhit += 10;}

	if($eid){
			($esk[0],$esk[1]) = split(/,/,$esk);
	        ($tmp_arm_sk2[0],$tmp_arm_sk2[1]) = split(/:/,$earmsta);
	        ($tmp_pro_sk2[0],$tmp_pro_sk2[1]) = split(/:/,$eprosta);
	        ($tmp_acc_sk2[0],$tmp_acc_sk2[1]) = split(/:/,$eaccsta);
	        ($tmp_pet_sk2[0],$tmp_pet_sk2[1]) = split(/:/,$epetsta);
	
		($earmno,$earmname,$earmval,$earmdmg,$earmwei,$earmele,$earmhit,$earmcl,$earmsta,$earmtype,$earmflg) = split(/,/,$earm);
		($eprono,$eproname,$eproval,$eprodmg,$eprowei,$eproele,$eprohit,$eprocl,$eprosta,$eprotype,$eproflg) = split(/,/,$epro);
		($eaccno,$eaccname,$eaccval,$eaccdmg,$eaccwei,$eaccele,$eacchit,$eacccl,$eaccsta,$eacctype,$eaccflg) = split(/,/,$eacc);
                ($epetno,$epetname,$epetdmg,$epetdef,$epetspeed,$epetele,$epetlv,$epetcl,$epetsta,$epettype,$epetflg) = split(/,/,$epet);

		if($esk[0] eq "62" || $esk[1] eq "62"){$eleplus2=0.2;}
		elsif($tmp_arm_sk2[0] eq "62" || $tmp_arm_sk2[1] eq "62"){$eleplus2 = 0.2;}
		elsif($tmp_pro_sk2[0] eq "62" || $tmp_pro_sk2[1] eq "62"){$eleplus2 = 0.2;}
		elsif($tmp_acc_sk2[0] eq "62" || $tmp_acc_sk2[1] eq "62"){$eleplus2 = 0.2;}
		elsif($tmp_pet_sk2[0] eq "62" || $tmp_pet_sk2[1] eq "62"){$eleplus2 = 0.2;}
        	if ($epet eq""){
	                $epetdmg=0;
                	$epetdef=0;
        	        $epetspeed=0;
	        }else{
        	        $epetname2="<font color=blue>+$epetname.lv$epetlv</font>";
	        }
		$ehpadd=0;
		if($eele eq "$earmele" && $earmele ne "0"){
			if($earmno eq"mix"){
				$earmdmg = int($earmdmg*(1.3 + $eleplus2));
			}else{
				$earmdmg = int($earmdmg*(1.2 + $eleplus2));
			}
		}
		if($eele eq "$eproele" && $eproele ne "0"){
			if($eprono eq"mix"){
				$eprodmg = int($eprodmg*(1.3 + $eleplus2));
			}else{
				$eprodmg = int($eprodmg*(1.2 + $eleplus2));
			}
		}
		if($eele eq "$eaccele" && $eaccele ne "0"){$eaccdmg = int($eaccdmg*(1.5 + $eleplus2));}
        	if($eele eq "$epetele" && $epetele ne "0"){
	                $epetdmg = int($epetdmg*(1.2 + $eleplus2));
                	$epetdef = int($epetdef*(1.2 + $eleplus2));
        	        $epetspeed = int($epetspeed*(1.2 + $eleplus2));
	        }

		if($ARM[$eclass] eq "$earmtype"){$earmhit += 10;}
	}
}

#################
##　隊伍裝備   ##
#################

sub unit_equip_open{
	$temp_unit_no=0;
	foreach(@unit_marm){
        ($t_unit_marmno,$t_unit_marmname,$t_unit_marmval,$t_unit_marmdmg,$t_unit_marmwei,$t_unit_marmele,$t_unit_marmhit,$t_unit_marmcl,$t_unit_marmsta,$t_unit_marmtype,$t_unit_marmflg) = split(/,/,$unit_marm[$temp_unit_no]);
        ($t_unit_mprono,$t_unit_mproname,$t_unit_mproval,$t_unit_mprodmg,$t_unit_mprowei,$t_unit_mproele,$t_unit_mprohit,$t_unit_mprocl,$t_unit_mprosta,$t_unit_mprotype,$t_unit_mproflg) = split(/,/,$unit_mpro[$temp_unit_no]);
        ($t_unit_maccno,$t_unit_maccname,$t_unit_maccval,$t_unit_maccdmg,$t_unit_maccwei,$t_unit_maccele,$t_unit_macchit,$t_unit_macccl,$t_unit_maccsta,$t_unit_macctype,$t_unit_maccflg) = split(/,/,$unit_macc[$temp_unit_no]);
        ($t_unit_mpetcno,$t_unit_mpetname,$t_unit_mpetdmg,$t_unit_mpetdef,$t_unit_mpetspeed,$t_unit_mpetele,$t_unit_mpetlv,$t_unit_mpetcl,$t_unit_mpetsta,$t_unit_mpettype,$t_unit_mpetflg) = split(/,/,$unit_mpet[$temp_unit_no]);
        ($unit_marmsta[$temp_unit_no],$unit_marmsta2[$temp_unit_no])=split(/:/,$t_unit_marmsta);
        ($unit_mprosta[$temp_unit_no],$unit_mprosta2[$temp_unit_no])=split(/:/,$t_unit_mprosta);
        ($unit_maccsta[$temp_unit_no],$unit_maccsta2[$temp_unit_no])=split(/:/,$t_unit_maccsta);
        ($unit_mpetsta[$temp_unit_no],$unit_mpetsta2[$temp_unit_no])=split(/:/,$t_unit_mpetsta);
        ($t_unit_msk[0],$t_unit_msk[1]) = split(/,/,$unit_msk[$temp_unit_no]);
	$eleplus=0;
        if($t_unit_msk[0] eq "62" || $t_unit_msk[1] eq "62"){$eleplus = 0.15;}
        if ($t_unit_mpet eq""){
                $t_unit_mpetdmg=0;
                $t_unit_mpetdef=0;
                $t_unit_mpetspeed=0;
        }
        if($unit_mele[$temp_unit_no] eq "$t_unit_marmele" && $t_unit_marmele ne "0"){$t_unit_marmdmg = int($t_unit_marmdmg*(1.2 + $eleplus));}
        if($unit_mele[$temp_unit_no] eq "$t_unit_mproele" && $t_unit_mproele ne "0"){$t_unit_mprodmg = int($t_unit_mprodmg*(1.2 + $eleplus));}
        if($unit_mele[$temp_unit_no] eq "$t_unit_maccele" && $t_unit_maccele ne "0"){$t_unit_maccdmg = int($t_unit_maccdmg*(1.5 + $eleplus));}
        if($unit_mele[$temp_unit_no] eq "$t_unit_mpetele" && $t_unit_mpetele ne "0"){
                $t_unit_mpetdmg = int($t_unit_mpetdmg*(1.2 + $eleplus));
                $t_unit_mpetdef = int($t_unit_mpetdef*(1.2 + $eleplus));
                $t_unit_mpetspeed = int($t_unit_mpetspeed*(1.2 + $eleplus));
        }
        $unit_mpetdmg+=$t_unit_mpetdmg;
        $unit_mpetdef+=$t_unit_mpetdef;
        $unit_mpetspeed+=$t_unit_mpetspeed;
        $unit_marmdmg+=$t_unit_marmdmg;
        $unit_mprodmg+=$t_unit_mprodmg;
        $unit_maccdmg+=$t_unit_maccdmg;
        $temp_unit_no++;
    }
}


sub status_print{
	open(IN,"./logfile/battle/$in{'id'}.cgi");
	@BC_DATA = <IN>;
	close(IN);
	($mhpr,$mmpr,$mtim)=split(/<>/,$BC_DATA[0]);
	if($mhpr eq""){$mhpr=1;}
	if($mmpr eq""){$mmpr=1;}
	$mken=$mhpr*100;

	$STPR= <<"_STATUS_";
	<TABLE border="0"cellspacing="2" CLASS=MC>
        <TBODY>
          <TR>
          <TD colspan="2" rowspan="4" bgcolor="$ELE_C[$mele]" align=center><img src="$IMG/chara/$mchara.gif"></TD>
          <TD bgcolor="$ELE_C[$mele]"><font size=2>名稱</font></TD>
          <TD colspan="2" bgcolor="$ELE_C[$mele]"><font size=2>$mname</font></TD>
          <TD bgcolor="$ELE_C[$mele]"><font size=2>LV</TD>
          <TD colspan="2" bgcolor="$ELE_C[$mele]"><font size=2>$mlv</font></TD>
          <TD bgcolor="$ELE_C[$mele]"><font size=2>性別</TD>
          <TD colspan="2" bgcolor="$ELE_C[$mele]"><font size=2>$SEX[$msex]</font></TD>
          </TR>
          <TR>
          <TD bgcolor="$ELE_C[$mele]"><font size=2>HP</TD>
          <TD colspan="2" bgcolor="$ELE_C[$mele]"><font size=2>$mhp/$mmaxhp</font></TD>
          <TD bgcolor="$ELE_C[$mele]"><font size=2>MP</TD>
          <TD colspan="2" bgcolor="$ELE_C[$mele]"><font size=2>$mmp/$mmaxmp</font></TD>
          <TD bgcolor="$ELE_C[$mele]"><font size=2>健康度</TD>
          <TD colspan="2" bgcolor="$ELE_C[$mele]"><font size=2>$mken %</font></TD>
          </TR>
          <TR>
          <TD bgcolor="$ELE_C[$mele]"><font size=2>經験值</font></TD>
          <TD colspan="2" bgcolor="$ELE_C[$mele]"><font size=2>$mex</font></TD>
          <TD bgcolor="$ELE_C[$mele]"><font size=2>職業</font></TD>
          <TD colspan="2" bgcolor="$ELE_C[$mele]"><font size=2>$JOB[$mclass]</font></TD>
          <TD bgcolor="$ELE_C[$mele]"><font size=2>熟練度</font></TD>
          <TD colspan="2" bgcolor="$ELE_C[$mele]"><font size=2>$mabp</font></TD>
          </TR>
	  <TR>
          <TD bgcolor="$ELE_C[$mele]"><font size=2>資金</font></TD>
          <TD colspan="2" bgcolor="$ELE_C[$mele]"><font size=2>$smgold</font></TD>
          <TD bgcolor="$ELE_C[$mele]"><font size=2>銀行</font></TD>
          <TD colspan="2" bgcolor="$ELE_C[$mele]"><font size=2>$smbank</font></TD>
          <TD bgcolor="$ELE_C[$mele]"><font size=2>名聲</font></TD>
          <TD colspan="2" bgcolor="$ELE_C[$mele]"><font size=2>$mcex</font></TD>
          </TR>
        </TBODY>
      </TABLE>
_STATUS_
}

##街データ読み込み
sub town_open{
	open(IN,"./data/towndata.cgi") or &error("城鎮資料開啟錯誤：sub.cgi(240)。");
	@TOWN_DATA = <IN>;
	close(IN);

	$t_no = 0;
	foreach(@TOWN_DATA){
		($town_id,$town_name,$town_con,$town_ele,$town_gold,$town_arm,$town_pro,$town_acc,$town_ind,$town_tr,$town_s,$town_x,$town_y,$town_build,$town_etc)=split(/<>/);
		if("$town_id" eq "$mpos"){last;$hit=1;}
		$t_no++;
	}
        ($town_hp,$town_max,$town_str,$town_def,$town_dex,$town_flg,$town_sta,$town_mix_lv[1],$town_mix_lv[2],$town_mix_lv[3],$town_mix_lv[4],$town_mix_lv[5],$town_mix_lv[6],$town_mix_lv[7],$town_mix[1],$town_mix[2],$town_mix[3],$town_mix[4],$town_mix[5],$town_mix[6],$town_mix[7])=split(/,/,$town_etc);
	($town_build_data[0],$town_build_data[1],$town_build_data[2],$town_build_data[3],$town_build_data[4],$town_build_data[5],$town_build_data[6],$town_build_data[7],$town_build_data[8],$town_build_data[9],$town_build_data[10],$town_build_data[11],$town_build_data[12])=split(/,/,$town_build);
}

###街データ書き込み
sub town_input{
	$town_etc="$town_hp,$town_max,$town_str,$town_def,$town_dex,$town_flg,$town_sta,$town_mix_lv[1],$town_mix_lv[2],$town_mix_lv[3],$town_mix_lv[4],$town_mix_lv[5],$town_mix_lv[6],$town_mix_lv[7],$town_mix[1],$town_mix[2],$town_mix[3],$town_mix[4],$town_mix[5],$town_mix[6],$town_mix[7]";
	$town_build="$town_build_data[0],$town_build_data[1],$town_build_data[2],$town_build_data[3],$town_build_data[4],$town_build_data[5],$town_build_data[6],$town_build_data[7],$town_build_data[8],$town_build_data[9],$town_build_data[10],$town_build_data[11],$town_build_data[12]";
	if($town_id ne ""){
		@NTOWN=();
		foreach(@TOWN_DATA){
			($town2_id,$town2_name,$town2_con,$town2_ele,$town2_gold,$town2_arm,$town2_pro,$town2_acc,$town2_ind,$town2_tr,$town2_s,$town2_x,$town2_y,$town2_build,$town2_etc)=split(/<>/);
			if("$town_id" eq "$town2_id"){
				push(@NTOWN,"$town_id<>$town_name<>$town_con<>$town_ele<>$town_gold<>$town_arm<>$town_pro<>$town_acc<>$town_ind<>$town_tr<>$town_s<>$town_x<>$town_y<>$town_build<>$town_etc<>\n");
			}else{
				push(@NTOWN,"$_");
			}
		}
		open(OUT,">./data/towndata.cgi") or &error('檔案無法開啟(sub.cgi)266。');
		print OUT @NTOWN;
		close(OUT);
		if(int(rand(20)) eq 1){
			open(OUT,">./data/towndata2.cgi");
			print OUT @NTOWN;
			close(OUT);
		}
	}
	else{&error("資料出現異常sub.cgi(275)。");}
}

###國データ
sub con_open{
	open(IN,"./data/country.cgi") or &error("國家資料開啟錯誤sub.cgi(280)。");
	@CON_DATA = <IN>;
	close(IN);

	$c_no = 0;
	foreach(@CON_DATA){
		($con_id,$con_name,$con_ele,$con_gold,$con_king,$con_yaku,$con_cou,$con_mes,$con_etc)=split(/<>/);
		if("$con_id" eq "$mcon"){$hit=1;last;}
		$c_no++;
	}
	if(!$hit){
		$con_id=0;$con_name="無所屬";
		$con_ele=0;$con_gold=0;
		$con_mes="";$con_etc=0;
		$con_king="";$con_yaku="";
	}
        $scon_gold=int($con_gold/10000);
        if ($scon_gold>9999) {
                $scon_gold=int($scon_gold/10000)."億".($scon_gold%10000)."萬";
        }elsif($con_gold<10000){
                $scon_gold="$con_gold Gold";
        }else{
                $scon_gold.="萬";
        }
	#Ajax國家情報
	$ajax_con_data="COUNTRY<>$con_id<>$con_name<>$con_ele<>$con_gold<>$con_king<>$con_yaku<>$con_cou<>$con_mes<>$con_etc";
	($y_name[0],$y_name[1],$y_name[2],$y_chara[0],$y_chara[1],$y_chara[2],$y_name[3],$y_name[4],$y_name[5],$y_chara[3],$y_chara[4],$y_chara[5])=split(/,/,$con_yaku);
}
sub con_input{
	if($con_id ne "" && $con_id ne 0){
		@NCON=();
		foreach(@CON_DATA){
			($con2_id,$con2_name,$con2_ele,$con2_gold,$con2_king,$con2_yaku,$con2_cou,$con2_mes,$con2_etc)=split(/<>/);
			if("$con_id" eq "$con2_id"){
				push(@NCON,"$con_id<>$con_name<>$con_ele<>$con_gold<>$con_king<>$con_yaku<>$con_cou<>$con_mes<>$con_etc<>\n");
			}else{
				push(@NCON,"$_");
			}
		}
		$NCONCOUNT=@NCON;
if($NCONCOUNT>=1){
		open(OUT,">./data/country.cgi") or &error('國家資料開啟錯誤sub.cgi(309)。');
		print OUT @NCON;
		close(OUT);
	}
}
}
##參加者リスト
sub guest_list {

	open(IN,"./data/guest_list.cgi");
	@guest = <IN>;
	close(IN);
	&host_name;
	$timer = time();@newguest=();
	foreach(@guest) {
		($gname,$gtime,$gcon,$ghost,$gid)=split(/<>/);
		if($timer>$gtime+($CMDTIME*100)){next;}
		elsif($mname eq $gname){
			#if($timer<$gtime+3){&error("操作過快,每次操作時間為$CMDTIME秒");}
			if($timer<$gtime+3){&error("操作過快,每次操作時間為3秒");}
			$ghit=1;
			push(@newguest,"$mname<>$timer<>$con_ele<>$host<>$mid<>\n");

#"<a href=\"javascript:void(0);\" onClick=\"window.open('./status_print.cgi?id=$pid', 'newwin', 'width=600,height=400,scrollbars =yes')\"><font color=$ELE_BG[$gcon]>$mname</a></font>";
#			$guestlist.="<font color=$ELE_BG[$gcon]>★$mname</font>";
$pid = &id_change("$mid");
			$guestlist.="★<a href=\"javascript:void(0);\" onClick=\"window.open('./status_print.cgi?id=$pid', 'newwin', 'width=600,height=400,scrollbars =yes')\"><font color=$ELE_BG[$gcon]>$mname</a></font>";
		}
		else{
$pid = &id_change("$gid");
			push(@newguest,"$gname<>$gtime<>$gcon<>$ghost<>$gid<>\n");
			$guestlist.="★<a href=\"javascript:void(0);\" onClick=\"window.open('./status_print.cgi?id=$pid', 'newwin', 'width=600,height=400,scrollbars =yes')\"><font color=$ELE_BG[$gcon]>$gname</a></font>";
		}
	}
	if(!$ghit){
		push(@newguest,"$mname<>$timer<>$con_ele<>$host<>$mid<>\n");
		$guestlist.="<font color=$ELE_BG[$mcon]>★$mname</font>";
	}
	open(OUT,">./data/guest_list.cgi") or &error('檔案無法開啟(sub.cgi)340。');
	print OUT @newguest;
	close(OUT);

}

###時間取得
sub time_data{
	$tt = time ;
	($sec,$min,$hour,$mday,$mon,$year,$wday,$yday) = localtime(time);
	$year += 1900;
	$mon++;
	$ww = (Sun,Mon,Tue,Wed,Thu,Fri,Sat)[$wday];
	$daytime = sprintf("%4d\/%02d\/%02d\/(%s)　%02d時%02d分", $year,$mon,$mday,$ww,$hour,$min);
}
sub time_data2{
        ($sec,$min,$hour,$mday,$mon,$year,$wday,$yday) = localtime($tt);
        $year += 1900;
        $mon++;
        $ww = (Sun,Mon,Tue,Wed,Thu,Fri,Sat)[$wday];
        $daytime = sprintf("%4d\/%02d\/%02d\/(%s)　%02d時%02d分", $year,$mon,$mday,$ww,$hour,$min);
}

###文字関係
sub decode{
	if ($ENV{'REQUEST_METHOD'} eq "POST") {
		read(STDIN, $buffer, $ENV{'CONTENT_LENGTH'});
	}else{$buffer = $ENV{'QUERY_STRING'}; }
	@buffer = split(/&/, $buffer);

	foreach (@buffer) {
	
		($na, $val) = split(/=/, $_);
		$val =~ tr/+/ /;
		$val =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C",hex($1))/eg;
		
		# 文字コードをシフトJIS変換
		&jcode'convert(*val, "sjis", "", "z");

		# タグ處理
		$val =~ s/</&lt;/g;
		$val =~ s/>/&gt;/g;
		$val =~ s/\"/&quot;/g;

		# 改行等處理
		if ($na eq "message") {
			$val =~ s/\r\n/<br>/g;
			$val =~ s/\r/<br>/g;
			$val =~ s/\n/<br>/g;
		} else {
			$val =~ s/\r//g;
			$val =~ s/\n//g;
		}
		$in{$na} = $val;
	}
}

##ホスト取得
sub host_name {

	$host = $ENV{'REMOTE_HOST'};
	$addr = $ENV{'REMOTE_ADDR'};

	if ($get_remotehost) {
		if ($host eq "" || $host eq "$addr") {
			$host = gethostbyaddr(pack("C4", split(/\./, $addr)), 2);
		}
	}
	if ($host eq "") { $host = $addr; }

}
sub error {
        &header;
        print <<"EOF";
        <center>
        <TABLE border="0" width="50%" bgcolor="#660000" CLASS=TC>
        <TBODY>
        <TR>
        <TD align="center"><FONT color="#ffffcc"><B>ＥＲＲＯＲ</B></FONT></TD>
        </TR>
        <TR>
        <TD bgcolor="#ffffff" align="center"><BR><B>$_[0]</B>
        <CENTER>
<input type="button" value="返回" CLASS=FC onclick="javascript:parent.backtown();">
        </CENTER>
        </TD>
        </TR>
        </TBODY>
        </TABLE>
        </CENTER>
        <BR><BR>
        </form>
        <P><hr size=0></center>
        </center>
EOF
        &footer;
        exit;
}
sub error2 {
        &header;
        print <<"EOF";
        <center>
        <TABLE border="0" width="50%" bgcolor="#660000" CLASS=TC>
        <TBODY>
        <TR>
        <TD align="center"><FONT color="#ffffcc"><B>ＥＲＲＯＲ</B></FONT></TD>
        </TR>
        <TR>
        <TD bgcolor="#ffffff" align="center"><BR><B>$_[0]</B>
        </TD>
        </TR>
        </TBODY>
        </TABLE>
        </CENTER>
        <BR><BR>
        <P><hr size=0></center>
        </center>
EOF
        &footer;
        exit;
}
sub error3 {
        &header;
        print <<"EOF";
        <center>
        <TABLE border="0" width="50%" bgcolor="#660000" CLASS=TC>
        <TBODY>
        <TR>
        <TD align="center"><FONT color="#ffffcc"><B>ＥＲＲＯＲ</B></FONT></TD>
        </TR>
        <TR>
        <TD bgcolor="#ffffff" align="center"><BR><B>$_[0]</B>
        </TD>
        </TR>
        </TBODY>
        </TABLE>
        </CENTER>
        <BR><BR>
        <P><hr size=0></center>
        </center>
<script language=javascript>
alert('$_[0]');
parent.location.href='index.cgi';
</script>
EOF
        &footer;
        exit;
}

sub error_old {
        &header;
        print <<"EOF";
        <center>
        <TABLE border="0" width="50%" bgcolor="#660000" CLASS=TC>
        <TBODY>
        <TR>
        <TD align="center"><FONT color="#ffffcc"><B>ＥＲＲＯＲ</B></FONT></TD>
        </TR>
        <TR>
        <TD bgcolor="#ffffff" align="center"><BR><B>$_[0]</B>
        <CENTER>
<form action="./top.cgi" method="POST">
        <INPUT type=hidden name=id value=$mid>
        <INPUT type=hidden name=pass value=$mpass><input type=hidden name=rmode value=$in{'rmode'}>

        <INPUT type=submit CLASS=FC value=回到城鎮>
</Form>
        </CENTER>
        </TD>
        </TR>
        </TBODY>
        </TABLE>
        </CENTER>
        <BR><BR>
        </form>
        <P><hr size=0></center>
        </center>
EOF
        &footer;
        exit;
}

#rエラー
sub error_alert {
        &header;
        print <<"EOF";
<script language="javascript">
alert('$_[0]');
</script>
EOF
        &footer;
        exit;
}
sub aerror {
    print "Cache-Control: no-cache\n";
    print "Pragma: no-cache\n";
    print "Content-type: text/html\n\n";
	print <<"EOF";
ERROR<>$_[0]

EOF
	exit;
}
sub aerror2 {
    print "Cache-Control: no-cache\n";
    print "Pragma: no-cache\n";
    print "Content-type: text/html\n\n";
	print <<"EOF";
ERROR2<>$_[0]

EOF
	exit;
}
##展開任務資料
sub quest_open{
        ($quest_town_no,$quest_town_name)=split(/:/,$ext_quest_town);
        ($quest_count[0],$quest_count[1],$quest_count[2],$quest_count[3],$quest_count[4],$quest_count[5],$quest_count[6],$quest_count[7],$quest_count[8])=split(/:/,$ext_quest_count);
        ($quest_etc[0],$quest_etc[1],$quest_etc[2],$quest_etc[3],$quest_etc[4],$quest_etc[5],$quest_etc[6],$quest_etc[7],$quest_etc[8])=split(/:/,$ext_quest_etc);
        ($quest_time[0],$quest_time[1],$quest_time[2],$quest_time[3],$quest_time[4],$quest_time[5],$quest_time[6],$quest_time[7],$quest_time[8])=split(/:/,$ext_quest_time);
	($quest1_limit_time,$quest1_town_no,$quest1_town_name,$quest1_item)=split(/;/,$quest_etc[1]);
        ($quest2_limit_time,$quest2_town_no,$quest2_town_name,$quest2_map,$quest2_count)=split(/;/,$quest_etc[2]);
	($quest5_limit_time,$quest5_town_no,$quest5_town_name,$quest5_mix)=split(/;/,$quest_etc[5]);
}
##結合任務資料
sub quest_input{
	$quest_etc[1]="$quest1_limit_time;$quest1_town_no;$quest1_town_name;$quest1_item";
        $quest_etc[2]="$quest2_limit_time;$quest2_town_no;$quest2_town_name;$quest2_map;$quest2_count";
	$quest_etc[5]="$quest5_limit_time;$quest5_town_no;$quest5_town_name;$quest5_mix";
	$ext_quest_town="$quest_town_no:$quest_town_name";
	$ext_quest_count="$quest_count[0]:$quest_count[1]:$quest_count[2]:$quest_count[3]:$quest_count[4]:$quest_count[5]:$quest_count[6]:$quest_count[7]:$quest_count[8]";
	$ext_quest_time="$quest_time[0]:$quest_time[1]:$quest_time[2]:$quest_time[3]:$quest_time[4]:$quest_time[5]:$quest_time[6]:$quest_time[7]:$quest_time[8]";
	$ext_quest_etc="$quest_etc[0]:$quest_etc[1]:$quest_etc[2]:$quest_etc[3]:$quest_etc[4]:$quest_etc[5]:$quest_etc[6]:$quest_etc[7]:$quest_etc[8]";
}
##開啟角色擴充欄
sub ext_open{
        open(IN,"./logfile/ext/$mid.cgi");
        @EXT_DATA = <IN>;
        close(IN);
        ($ext_storageadd,$vertime,$nowmap,$down_lv_limit,$member_point,$member_auto_sleep,$member_auto_savegold,$member_fix_time,$member_mix,$member_point_total,$ext_show_mode,$ext_kinghp,$ext_kingetc,$ext_robot_count,$ext_lock,$ext_mixs,$ext_total,$ext_entry_count,$ext_today_count,$ext_check_robot,$ext_para_add,$ext_action,$ext_quest,$ext_w,$ext_x,$ext_y,$ext_z) = split(/<>/,$EXT_DATA[0]);
	($ext_show_mode_maplog,$ext_show_mode_guest)=split(/,/,$ext_show_mode);
	($ext_robot,$ext_robot_1,$ext_robot_2,$ext_robot_3)=split(/,/,$ext_robot_count);
	($ext_mix[0],$ext_mix[1],$ext_mix[2],$ext_mix[3],$ext_mix[4],$ext_mix[5],$ext_mix[6],$ext_mix[7],$ext_ab_item[0],$ext_ab_item[1],$ext_ab_item[2],$ext_ab_item[3],$ext_ab_item[4],$ext_ab_item[5])=split(/,/,$ext_mixs);
	if($ext_storageadd eq""){
		$ext_storageadd=0;
	}
	if($member_point_total eq""){
		$member_point_total=0;
	}
	if ($member_point_total ne"" && $member_point_total ne"0"){
		$member_level=int($member_point_total/1000)+1;
	}else{
		$member_level=0;
	}
	$STORITM_MAX+=$ext_storageadd;
	($ext_quest_town,$ext_quest_total,$ext_quest_count,$ext_quest_time,$ext_quest_etc)=split(/,/,$ext_quest);

}
##開啟其他角色擴充欄
sub ext_enemy_open{
        open(IN,"./logfile/ext/$enemy_id.cgi");
        @ext2_DATA = <IN>;
        close(IN);
        ($ext2_storageadd,$vertime2,$nowmap2,$down2_lv_limit,$member2_point,$member2_auto_sleep,$member2_auto_savegold,$member2_fix_time,$member2_mix,$member2_point_total,$ext2_show_mode,$ext2_kinghp,$ext2_kingetc,$ext2_robot_count,$ext2_lock,$ext2_mixs,$ext2_total,$ext2_entry_count,$ext2_today_count,$ext2_check_robot,$ext2_para_add,$ext2_action,$ext2_quest,$ext2_w,$ext2_x,$ext2_y,$ext2_z) = split(/<>/,$ext2_DATA[0]);
        ($ext2_show_mode_maplog,$ext2_show_mode_guest)=split(/,/,$ext2_show_mode);
        ($ext2_robot,$ext2_robot_1,$ext2_robot_2,$ext2_robot_3)=split(/,/,$ext2_robot_count);
	($ext2_mix[0],$ext2_mix[1],$ext2_mix[2],$ext2_mix[3],$ext2_mix[4],$ext2_mix[5],$ext2_mix[6],$ext2_mix[7],$ext2_ab_item[0],$ext2_ab_item[1],$ext2_ab_item[2],$ext2_ab_item[3],$ext2_ab_item[4],$ext2_ab_item[5])=split(/,/,$ext2_mixs);
        if($ext2_storageadd eq""){
                $ext2_storageadd=0;
        }
        if($member2_point_total eq""){
                $member2_point_total=0;
        }
        $STORITM2_MAX+=$ext2_storageadd;

}

##儲存角色擴充欄
sub ext_input{
        @N_DATA=();
	$ext_show_mode="$ext_show_mode_maplog,$ext_show_mode_guest";
	$ext_robot_count="$ext_robot,$ext_robot_1,$ext_robot_2,$ext_robot_3";
	$ext_mixs="$ext_mix[0],$ext_mix[1],$ext_mix[2],$ext_mix[3],$ext_mix[4],$ext_mix[5],$ext_mix[6],$ext_mix[7],$ext_ab_item[0],$ext_ab_item[1],$ext_ab_item[2],$ext_ab_item[3],$ext_ab_item[4],$ext_ab_item[5]";
	$ext_quest="$ext_quest_town,$ext_quest_total,$ext_quest_count,$ext_quest_time,$ext_quest_etc";
        unshift(@N_DATA,"$ext_storageadd<>$vertime<>$nowmap<>$down_lv_limit<>$member_point<>$member_auto_sleep<>$member_auto_savegold<>$member_fix_time<>$member_mix<>$member_point_total<>$ext_show_mode<>$ext_kinghp<>$ext_kingetc<>$ext_robot_count<>$ext_lock<>$ext_mixs<>$ext_total<>$ext_entry_count<>$ext_today_count<>$ext_check_robot<>$ext_para_add<>$ext_action<>$ext_quest<>$ext_w<>$ext_x<>$ext_y<>$ext_z<><>\n");
        open(OUT,">./logfile/ext/$mid.cgi");
        print OUT @N_DATA;
        close(OUT);

}
##儲存其他角色擴充欄
sub ext_enemy_input{
        @N_DATA=();
        $ext2_show_mode="$ext2_show_mode_maplog,$ext2_show_mode_guest";
        $ext2_robot_count="$ext2_robot,$ext2_robot_1,$ext2_robot_2,$ext2_robot_3";
	$ext2_mixs="$ext2_mix[0],$ext2_mix[1],$ext2_mix[2],$ext2_mix[3],$ext2_mix[4],$ext2_mix[5],$ext2_mix[6],$ext2_mix[7],$ext2_ab_item[0],$ext2_ab_item[1],$ext2_ab_item[2],$ext2_ab_item[3],$ext2_ab_item[4],$ext2_ab_item[5]";
        unshift(@N_DATA,"$ext2_storageadd<>$vertime2<>$nowmap2<>$down2_lv_limit<>$member2_point<>$member2_auto_sleep<>$member2_auto_savegold<>$member2_fix_time<>$member2_mix<>$member2_point_total<>$ext2_show_mode<>$ext2_kinghp<>$ext2_kingetc<>$ext2_robot_count<>$ext2_lock<>$ext2_mixs<>$ext2_total<>$ext2_entry_count<>$ext2_today_count<>$ext2_check_robot<>$ext2_para_add<>$ext2_action<>$ext2_quest<>$ext2_w<>$ext2_x<>$ext2_y<>$ext2_z<><>\n");
        open(OUT,">./logfile/ext/$enemy_id.cgi");
        print OUT @N_DATA;
        close(OUT);

}

##開啟其他擴充
sub fixext_open{
    open(IN,"./logfile/fixext/$mid.cgi");
    @FIXEXT_DATA = <IN>;
    close(IN);
    ($fixext_fastkey,$fixext_b,$fixext_c,$fixext_d,$fixext_e,$fixext_f,$fixext_g,$fixext_h,$fixext_i,$fixext_j,$fixext_k,$fixext_l,$fixext_m,$fixext_n,$fixext_o,$fixext_p,$fixext_q,$fixext_r,$fixext_s,$fixext_t,$fixext_u,$fixext_v,$fixext_w,$fixext_x,$fixext_y,$fixext_z) = split(/<>/,$FIXEXT_DATA[0]);
    ($fixext_fkey[0],$fixext_fkey[1],$fixext_fkey[2],$fixext_fkey[3],$fixext_fkey[4],$fixext_fkey[5],$fixext_fkey[6],$fixext_fkey[7],$fixext_fkey[8],$fixext_fkey[9])=split(/;/,$fixext_fastkey);
}
##關閉其他擴充
sub fixext_input{
	@N_DATA=();
    $fixext_fastkey="$fixext_fkey[0];$fixext_fkey[1];$fixext_fkey[2];$fixext_fkey[3];$fixext_fkey[4];$fixext_fkey[5];$fixext_fkey[6];$fixext_fkey[7];$fixext_fkey[8];$fixext_fkey[9]";
	unshift(@N_DATA,"$fixext_fastkey<>$fixext_b<>$fixext_c<>$fixext_d<>$fixext_e<>$fixext_f<>$fixext_g<>$fixext_h<>$fixext_i<>$fixext_j<>$fixext_k<>$fixext_l<>$fixext_m<>$fixext_n<>$fixext_o<>$fixext_p<>$fixext_q<>$fixext_r<>$fixext_s<>$fixext_t<>$fixext_u<>$fixext_v<>$fixext_w<>$fixext_x<>$fixext_y<>$fixext_z<><>\n");
    open(OUT,">./logfile/fixext/$mid.cgi");
    print OUT @N_DATA;
    close(OUT);
}

sub id_change {
	local($inpw) = $_[0];

	@yy = unpack("C*", $inpw);
	$word="";
	foreach(@yy){
		$word .= "$_\,";
	}
	chomp($word);
	$encrypt = reverse($word);

	return $encrypt;
}
sub header{
	print "Cache-Control: no-cache\n";
	print "Pragma: no-cache\n";
	print "Content-type: text/html\n\n";
	print <<"EOF";
<html>
<head>
<META HTTP-EQUIV="Content-type" CONTENT="text/html; charset=utf-8">
<STYLE type="text/css">
<!--
body, td { font-size:12px}
A:HOVER{
 color: blue;
}
.BC {border-top-width : medium;border-right-width : medium;border-bottom-width : medium;border-left-width :medium; border-color : $ELE_BG[0] $ELE_BG[0] $ELE_BG[0] $ELE_BG[0];border-style : double double double double;background-color : $ELE_BG[0];color: black;}
.TC {border-top-width : medium;border-right-width : medium;border-bottom-width : medium;border-left-width :medium; border-color : $FCOLOR $FCOLOR $FCOLOR $FCOLOR;border-style : double double double double;background-color : $FCOLOR;color : black;}
.CC {border-top-width : medium;border-right-width : medium;border-bottom-width : medium;border-left-width :medium; border-color : $ELE_BG[$con_ele] $ELE_BG[$con_ele] $ELE_BG[$con_ele] $ELE_BG[$con_ele];border-style : double double double double;background-color : $ELE_BG[$con_ele];color : black;}
.CC2 {border-top-width : medium;border-right-width : medium;border-bottom-width : medium;border-left-width :medium; border-color : $ELE_BG[$con2_ele] $ELE_BG[$con2_ele] $ELE_BG[$con2_ele] $ELE_BG[$con2_ele];border-style : double double double double;background-color : $ELE_BG[$con2_ele];color : black;}
.MC {border-top-width : medium;border-right-width : medium;border-bottom-width : medium;border-left-width :medium; border-color : $ELE_BG[$mele] $ELE_BG[$mele] $ELE_BG[$mele] $ELE_BG[$mele];border-style : double double double double;background-color : $ELE_BG[$mele];color : black;}
.MFC {border-top-width : medium;border-right-width : medium;border-bottom-width : medium;border-left-width :medium; border-top-color : $ELE_BG[$con_ele];border-right-color : $ELE_BG[$con_ele];border-bottom-color : $ELE_BG[$con_ele];border-left-color : $ELE_BG[$con_ele];border-style : double double double double;background-color : $ELE_C[$con_ele];color : black;}
.FC {border-top-width : medium;border-right-width : medium;border-bottom-width : medium;border-left-width : medium;border-top-color : $FCOLOR;border-right-color : $FCOLOR;border-bottom-color : $FCOLOR;border-left-color : $FCOLOR;border-style : double double double double;background-color : $FCOLOR2;color : black;}
.TOC {border-top-width : medium;border-right-width : medium;border-bottom-width : medium;border-left-width :medium; border-color : $ELE_BG[$town_ele] $ELE_BG[$town_ele] $ELE_BG[$town_ele] $ELE_BG[$town_ele];border-style : double double double double;background-color : $ELE_BG[$town_ele];color : black;}
.dmg { color: #FF0000; font-size: 10pt }
.clit { color: #0000FF; font-size: 10pt }
-->
</STYLE>


EOF

	#if($tmode eq "timer"){
	#if($s_time > 0){
	#}

	#}
	
	print "<title>$TITLE</title>\n";
	print "</head>";
	print "<body background=\"$BGIF\" bgcolor=\"$BG\" topmargin=\"0\" leftmargin=\"0\" rightmargin=\"0\" bottommargin=\"0\" marginwidth=\"0\" marginheight=\"0\">";
}

sub footer{
	print <<"EOF";
<script language="javascript">
	parent.scrollToTop.action();
function keyDownHandler(e) {
    if (e) { // Firefox
        if(e.keyCode==115){
                parent.backtown();
                e.preventDefault();
                e.stopPropagation();
        }
    } else { // IE
        if(window.event.keyCode == 115){
                window.event.keyCode = 0;
                parent.backtown();
                return false;
        }
    }
}
document.onkeydown = keyDownHandler;
</script>
	</body>
	</html>
EOF
}
sub mainfooter{
        print <<"EOF";
        <DIV align=center>
        <font size=2 color=#FFFFFF>
        $VER <A HREF="http://farland.jellybean.jp/top.htm" target="blank"><FONT size="2" color="#ffff99">bean</font></a><BR>
        參考：The Wars of Roses Ver6.4 <a href=\"http://g2.ngw.jp/~maccyu/game/\" target="blank"><FONT size="2" color="#ffff99">maccyu</font></a><br>
        繁體中文化無限改版:<a href="http://www.gm.idv.tw/"><FONT size="2" color="#ffff99">Zeeman</font></a><br>
        <BR><BR></font>
        </body>
        </html>
EOF
}
sub createver {
                open(IN,"vercode.cgi");
                @VER_DATA = <IN>;
                close(IN);
                $vcode="";
                $ilen=int(rand(3))+4;
                for ($i=0;$i<$ilen;$i++){
                        ($vcodes[0],$vcodes[1])=split(/\n/,$VER_DATA[int(rand(1100))]);
                        $vcode.=$vcodes[0];
                }
                $ext_check_robot=$vcode;
}
sub vercheck_form {
        $date = time();
                $ext_tmpx2=$ext_lock-$date;
                $ext_tmpx=int(($ext_tmpx2)/60/60);
                if($ext_tmpx2>0){
&verchklog("封鎖後戰鬥($ext_robot)");
                        &error3("你的帳號已被封鎖,需要$ext_tmpx小時($ext_tmpx2秒)才會解除");
                }
        &header;

	$tts=time();
	$ntime=$tts-$vertime;
                $vrnd=int(rand(100));
                open(IN,"vercode.cgi");
                @VER_DATA = <IN>;
                close(IN);
                $vcode="";
        $VERRND=int(rand(6))+1;
        for ($x=1;$x<=6;$x++){
                $vcode="";
                $vcode3="";
                $ilen=int(rand(3))+4;
                for ($i=0;$i<$ilen;$i++){
                        ($vcodes[0],$vcodes[1])=split(/\n/,$VER_DATA[int(rand(1100))]);
                        $vcode.=$vcodes[0];
                }
                if($x eq $VERRND){
                        $vcode=$ext_check_robot;
                }
                if($vertime % 5 eq 1){
                        $VERBUTTON.="<input type=button Class=FC value=".$x."."."$vcode style=width:100px;height:50px onclick=javascript:submits$vrnd('$vcode') name=B1>　　";
                }else{
                        $VERBUTTON.=$x."."."$vcode<input type=button Class=FC style=width:100px;height:50px value=選擇 onclick=javascript:submits$vrnd('$vcode') name=B1>　　　";
                }
		if($x %3 eq 0){$VERBUTTON.="<BR><BR>";}
        }
                $vertime=$tts;
                &ext_input;
        print <<"EOF";
        <center>
        <TABLE border="0" width="100%" bgcolor="#660000" CLASS=TC height=900 onclick="verlog('click');">
        <TBODY>
        <TR>
        <TD valign=top height=40 align="center" style="color:#FFFFCC"><B><font size=5>外掛驗證</font><BR></B><B>請盡快選擇與下方句子一樣的選項<BR></B></TD>
        </TR>
        <TR>
        <TD valign=top height=50 align="center" style="color:#EEEECC;"><B><IMG src="/showver.php?ver=$mid&check=$vertime" border=0></B></TD>
        </TR>
        <TR>
        <TD bgcolor="#ffffff" valign=top align="center"><BR><B>$_[0]</B>
        <CENTER>
$VERBUTTON
        </CENTER>
        </TD>
        </TR>
        </TBODY>
        </TABLE>
        </CENTER>
        <BR><BR>
        </form>
        <P><hr size=0></center>
        </center>
                <form action=./battle.cgi method=post id=battlef$vrnd target=actionframe>
                <input type=hidden name=id value=$mid>
                <INPUT type=hidden name=pass value=$mpass>
                <input type=hidden name=rmode value=$in{'rmode'}>
                <input type=hidden name=mode value=$in{'mode'}>
                <input type=hidden name=rnd value=$moya>
                <input type=hidden name=rnd2 value=$moya>
                <input type=hidden name=verchk>
                </form>
<form target=_top action=/index.html id=outf>
<form>
<script language=javascript>
function submits$vrnd(v){
        battlef$vrnd.verchk.value=v;
        battlef$vrnd.submit();
}
function GetXmlHttpObject(){
        var xmlHttp=null;
        try
          {
          // Firefox, Opera 8.0+, Safari
          xmlHttp=new XMLHttpRequest();
          }
        catch (e)
          {
          // Internet Explorer
          try
            {
            xmlHttp=new ActiveXObject("Msxml2.XMLHTTP");
            }
          catch (e)
            {
            xmlHttp=new ActiveXObject("Microsoft.XMLHTTP");
            }
          }
        return xmlHttp;
}
var cnt=2;
function verlog(opr){
        if(opr=='click'){cnt--;}
        if(opr=='click' && battlef$vrnd.verchk.value !=''){
        }else if(cnt<1 || opr==''){
        sid=Math.random();
        var url='';
        xmlHttp=GetXmlHttpObject();
        if (xmlHttp==null) {
                return;
        }
        url='verlog.cgi';
        params='id=$in{'id'}&pass=$in{'pass'}&sid='+sid+'&opr='+opr;
        xmlHttp.onreadystatechange=function(){
                if(xmlHttp.readyState==4 && xmlHttp.status == 200){
                        var d = xmlHttp.responseText;
                }else if(xmlHttp.readyState==2){

                }
        }

        if (url != '') {
                xmlHttp.open("POST",url,true);
                xmlHttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
                xmlHttp.setRequestHeader("Content-length", params.length);
                xmlHttp.setRequestHeader("Connection", "close");
                xmlHttp.send(params);
        }
        if(opr==''){
                setTimeout("verlog('');",60000);
        }
        }
}
setTimeout("verlog('');",60000);
</script>
EOF
        &footer;
        exit;
}
sub quest_form {
	&header;
        print <<"EOF";
        <center>
        <TABLE border="0" width="100%" bgcolor="#660000" CLASS=TC height=1>
        <TBODY>
        <TR>
        <TD valign=top height=40 align="center" style="color:#FFFFCC"><B><font size=5><font color=yellow>[$QUEST_NAME[0]]</font>$quest_town_name的村民有任務請求解決</font><BR></B><B>
        請到$quest_town_name的任務屋接受請求<BR>請於「其他」->「移動」選擇$quest_town_name，再按移動就可移動到該處</B></TD>
        <TR>
        </TABLE>
        $BACKTOWNBUTTON
EOF
        &footer;
        exit;
}

sub quest_form2 {
	&header;
	$ltime=$quest_time[0]-$date;
	if($ltime>0){
		$com="請$ltime秒內,";
	}else{
		$com="請";
	}
	($quest_town_no,$quest_town_name)=split(/:/,$ext_quest_town);
        print <<"EOF";
        <center>
        <TABLE border="0" width="100%" bgcolor="#660000" CLASS=TC height=1>
        <TBODY>
        <TR>
        <TD valign=top height=40 align="center" style="color:#FFFFCC"><B><font size=5><font color=yellow>[$QUEST_NAME[0]]</font>你已完成$quest_town_name村民交待的任務</font><BR></B><B>
        $com到任意城鎮的任務屋交還任務<BR></B></TD>
        <TR>
        </TABLE>
        $BACKTOWNBUTTON
EOF
        &footer;
        exit;
}


#if($ENV{'SERVER_NAME'} ne "www.gm.idv.tw"){&error2("請使用以下網址進入遊戲<BR><a href=\"http://www.gm.idv.tw/\" target=\"_top\">http://www.gm.idv.tw</a>");}
1;

