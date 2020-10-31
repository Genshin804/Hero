        $tt = time ;
        ($sec,$min,$hour,$mday,$mon,$year,$wday,$yday) = localtime(time);
        $year += 1900;
        $mon++;
        $wday++;
        $ww = (Sun,Mon,Tue,Wed,Thu,Fri,Sat)[$wday];
        $daytime = sprintf("%4d\/%02d\/%02d\/(%s)　%02d時%02d分", $year,$mon,$mday,$ww,$hour,$min);

open(IN,"/var/www/hero/data/towndata.cgi");
@T_LIST = <IN>;
close(IN);
$ti=0;
foreach(@T_LIST){
	($town_id,$town_name,$town_con,$town_ele,$town_gold,$town_arm,$town_pro,$town_acc,$town_ind,$town_tr,$town_s,$town_x,$town_y,$town_build,$town_etc)=split(/<>/);
        ($town_hp,$town_max,$town_str,$town_def,$town_dex,$town_flg,$town_sta,$town_mix_lv[1],$town_mix_lv[2],$town_mix_lv[3],$town_mix_lv[4],$town_mix_lv[5],$town_mix_lv[6],$town_mix_lv[7],$town_mix[1],$town_mix[2],$town_mix[3],$town_mix[4],$town_mix[5],$town_mix[6],$town_mix[7])=split(/,/,$town_etc);
	for($elei=1;$elei<8;$elei++){
		$town_mix[$elei]=$town_mix_lv[$elei];
	}
	$town_etc="$town_hp,$town_max,$town_str,$town_def,$town_dex,$town_flg,$town_sta,$town_mix_lv[1],$town_mix_lv[2],$town_mix_lv[3],$town_mix_lv[4],$town_mix_lv[5],$town_mix_lv[6],$town_mix_lv[7],$town_mix[1],$town_mix[2],$town_mix[3],$town_mix[4],$town_mix[5],$town_mix[6],$town_mix[7]";
	$T_LIST[$ti]="$town_id<>$town_name<>$town_con<>$town_ele<>$town_gold<>$town_arm<>$town_pro<>$town_acc<>$town_ind<>$town_tr<>$town_s<>$town_x<>$town_y<>$town_build<>$town_etc<>\n";
	$ti++;
}
        open(OUT,">/var/www/hero/data/towndata.cgi");
        print OUT @T_LIST;
        close(OUT);
                open(IN,"/var/www/hero/data/maplog.cgi");
                @data = <IN>;
                close(IN);
                unshift(@data, "<font color=green><b>[原料黑商]</b>各城鎮的原料黑商已經將貨物運送到達。</font>($daytime)\n");
                splice(@data,10);
                open (OUT, "> /var/www/hero/data/maplog.cgi");
                print OUT @data;

