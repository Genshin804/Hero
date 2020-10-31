#! /usr/bin/perl
require './jcode.pl';
require './sub.cgi';
require './conf.cgi';
        &header;
        print"<table CLASS=TC width=100%><td align=center><font color=$FCOLOR2 size=4>本月戰數排名</font></td></table><BR>";
        print"<center><a href=./jranking.cgi><font color=#FFFFFF><b>其他排名</b></font></a></center>";

        $dir="./logfile/ext";
        opendir(dirlist,"$dir");
        &time_data;
        $i=0;
        while($file = readdir(dirlist)){
                if($file =~ /\.cgi/i){
                        $datames = "查詢：$dir/$file<br>\n";
                        if(!open(cha,"$dir/$file")){
                                &error("$dir/$file&#12364;&#12415;&#12388;&#12363;&#12426;&#12414;&#12379;&#12435;。<br>\n");
                        }
                        @cha = <cha>;
                        close(cha);
                        $list[$i]="$file";
                        ($ext_storageadd,$vertime,$nowmap,$down_lv_limit,$member_point,$member_auto_sleep,$member_auto_savegold,$member_fix_time,$member_mix,$member_point_total,$ext_show_mode,$ext_kinghp,$ext_kingetc,$ext_robot_count,$ext_lock,$ext_mixs,$ext_total,$ext_q,$ext_r,$ext_s,$ext_t,$ext_u,$ext_v,$ext_w,$ext_x,$ext_y,$ext_z) = split(/<>/,$cha[0]);
                        ($ext_tl_chara,$ext_tl_name,$ext_tl_month,$ext_tl_type[0],$ext_tl_type[1],$ext_tl_type[2],$ext_tl_type[3],$ext_tl_type[4],$ext_tl_type[5],$ext_tl_king,$ext_tl_lose,$ext_tl_lvup,$ext_tl_gift,$ext_tl_mix,$ext_tl_rshop,$ext_tl_goditem)=split(/,/,$ext_total);
                        if ($ext_tl_month eq "$mon") {
                                $ext_tl_total=$ext_tl_type[0]+$ext_tl_type[1]+$ext_tl_type[2]+$ext_tl_type[3]+$ext_tl_type[4]+$ext_tl_type[5];
                               	if ($ext_tl_total eq "" || $ext_tl_total eq "0"){$ext_tl_total=1;}
                                if($ext_tl_gift eq "0" || $ext_tl_gift eq ""){
                                	$ext_tl_nolucky=0.5 / $ext_tl_total; 
                                }else{
                                	$ext_tl_nolucky=$ext_tl_gift / $ext_tl_total; 
                                }
                                $ext_tl_nolucky=1/$ext_tl_nolucky;
                                push(@CL_DATA,"$ext_tl_chara<>$ext_tl_name<>$ext_tl_month<>$ext_tl_type[0]<>$ext_tl_type[1]<>$ext_tl_type[2]<>$ext_tl_type[3]<>$ext_tl_type[4]<>$ext_tl_type[5]<>$ext_tl_king<>$ext_tl_lose<>$ext_tl_lvup<>$ext_tl_total<>$ext_tl_gift<>$ext_tl_mix<>$ext_tl_rshop<>$ext_tl_goditem<>$ext_tl_nolucky<>\n");
                        }
                }
                if($mn>10000){&error("&#12523;&#12540;&#12503;");}
                $mn++;
        }
        closedir(dirlist);


        @tmp1 = map {(split /<>/)[13]} @CL_DATA;
        @tmp2 = map {(split /<>/)[14]} @CL_DATA;
        @tmp3 = map {(split /<>/)[15]} @CL_DATA;
        @tmp4 = map {(split /<>/)[16]} @CL_DATA;
        @tmp5 = map {(split /<>/)[17]} @CL_DATA;
        @tmp6 = map {(split /<>/)[12]} @CL_DATA;
        @tmp7 = map {(split /<>/)[9]} @CL_DATA;
        @tmp8 = map {(split /<>/)[11]} @CL_DATA;
        @tmp9 = map {(split /<>/)[10]} @CL_DATA;
        @tmp10 = map {(split /<>/)[3]} @CL_DATA;
        @tmp11 = map {(split /<>/)[4]} @CL_DATA;
        @tmp12 = map {(split /<>/)[5]} @CL_DATA;
        @tmp13 = map {(split /<>/)[6]} @CL_DATA;
        @tmp14 = map {(split /<>/)[7]} @CL_DATA;
        @tmp15 = map {(split /<>/)[8]} @CL_DATA;
        
        @CL_DATA1 = @CL_DATA[sort {$tmp1[$b] <=> $tmp1[$a]} 0 .. $#tmp1];
        @CL_DATA2 = @CL_DATA[sort {$tmp2[$b] <=> $tmp2[$a]} 0 .. $#tmp2];
        @CL_DATA3 = @CL_DATA[sort {$tmp3[$b] <=> $tmp3[$a]} 0 .. $#tmp3];
        @CL_DATA4 = @CL_DATA[sort {$tmp4[$b] <=> $tmp4[$a]} 0 .. $#tmp4];
        @CL_DATA5 = @CL_DATA[sort {$tmp5[$b] <=> $tmp5[$a]} 0 .. $#tmp5];
        @CL_DATA6 = @CL_DATA[sort {$tmp6[$b] <=> $tmp6[$a]} 0 .. $#tmp6];
        @CL_DATA7 = @CL_DATA[sort {$tmp7[$b] <=> $tmp7[$a]} 0 .. $#tmp7];
        @CL_DATA8 = @CL_DATA[sort {$tmp8[$b] <=> $tmp8[$a]} 0 .. $#tmp8];
        @CL_DATA9 = @CL_DATA[sort {$tmp9[$b] <=> $tmp9[$a]} 0 .. $#tmp9];
        @CL_DATA10 = @CL_DATA[sort {$tmp10[$b] <=> $tmp10[$a]} 0 .. $#tmp10];
        @CL_DATA11 = @CL_DATA[sort {$tmp11[$b] <=> $tmp11[$a]} 0 .. $#tmp11];
        @CL_DATA12 = @CL_DATA[sort {$tmp12[$b] <=> $tmp12[$a]} 0 .. $#tmp12];
        @CL_DATA13 = @CL_DATA[sort {$tmp13[$b] <=> $tmp13[$a]} 0 .. $#tmp13];
        @CL_DATA14 = @CL_DATA[sort {$tmp14[$b] <=> $tmp14[$a]} 0 .. $#tmp14];
        @CL_DATA15 = @CL_DATA[sort {$tmp15[$b] <=> $tmp15[$a]} 0 .. $#tmp15];
        $sort_name[0]="打寶之王";
        $sort_name[1]="原料之王";
        $sort_name[2]="魔女最愛";
        $sort_name[3]="神武之王";
        $sort_name[4]="壞運之王";
        $sort_name[5]="總戰數之王";
        $sort_name[6]="砍王之王";
        $sort_name[7]="升級之王";
        $sort_name[8]="戰敗之王";
        $sort_name[9]="$TYPE[0]之王";
        $sort_name[10]="$TYPE[1]之王";
        $sort_name[11]="$TYPE[2]之王";
        $sort_name[12]="$TYPE[3]之王";
        $sort_name[13]="$TYPE[4]之王";
        $sort_name[14]="$TYPE[5]之王";
        for($i=0;$i<15;$i++){
                $con_table[$i].="<table CLASS=FC>";
                $con_table[$i].="<tr>";
                $con_table[$i].="<td colspan=4 align=center bgcolor=$ELE_BG[$con_ele]><font color=$FCOLOR2 size=5><b>$sort_name[$i]</b></font></td>";
                $con_table[$i].="</tr>";
                $con_table[$i].="<tr>";
                $con_table[$i].="<td width=25% CLASS=TC><font color=$FCOLOR2>順位</font></td><td width=25% CLASS=TC><font color=$FCOLOR2>名稱</font></td><td width=25% CLASS=TC><font color=$FCOLOR2>頭像</font></td><td width=25% CLASS=TC><font color=$FCOLOR2>戰數</font></td>";
                $con_no++;
        }
        $coui=0;
        foreach(@CL_DATA1){

                ($ext_tl_chara,$ext_tl_name,$ext_tl_month,$ext_tl_type[0],$ext_tl_type[1],$ext_tl_type[2],$ext_tl_type[3],$ext_tl_type[4],$ext_tl_type[5],$ext_tl_king,$ext_tl_lose,$ext_tl_lvup,$ext_tl_total,$ext_tl_gift,$ext_tl_mix,$ext_tl_rshop,$ext_tl_goditem,$ext_tl_nolucky) = split(/<>/);

                if($cont_cou[$coui]<10){
                        $cont_cou[$coui]++;
                        $rank="$cont_cou[$coui]位";
                        $sort_value=$ext_tl_gift;
                        if($cont_cou[$coui] eq 1){
                                $rank="<font color=red size=4><b>★$cont_cou[$coui]位</b></font>";
                                $sort_value="<font color=red size=4><b>$sort_value</b></font>";
                        }
                        elsif($cont_cou[$coui] < 4){
                                $rank="<font color=blue size=3><b>$cont_cou[$coui]位</b></font>";
                                $sort_value="<font color=blue size=3><b>$sort_value</b></font>";
                        }
                        $con_table[$coui].="<tr><td bgcolor=$ELE_C[$con_ele[0]] size=2>$rank</td><td bgcolor=$ELE_C[$con_ele[0]] size=2>$ext_tl_name</td><td bgcolor=$ELE_C[$con_ele[0]]><img width=35 height=35 src=\"$IMG/chara/$ext_tl_chara.gif\"></td><td bgcolor=$ELE_C[$con_ele[0]]>$sort_value</td></tr>";
                }else{last;}
        }
        $coui++;
        foreach(@CL_DATA2){
                ($ext_tl_chara,$ext_tl_name,$ext_tl_month,$ext_tl_type[0],$ext_tl_type[1],$ext_tl_type[2],$ext_tl_type[3],$ext_tl_type[4],$ext_tl_type[5],$ext_tl_king,$ext_tl_lose,$ext_tl_lvup,$ext_tl_total,$ext_tl_gift,$ext_tl_mix,$ext_tl_rshop,$ext_tl_goditem,$ext_tl_nolucky) = split(/<>/);

                if($cont_cou[$coui]<10){
                        $cont_cou[$coui]++;
                        $rank="$cont_cou[$coui]位";
                        $sort_value=$ext_tl_mix;
                        if($cont_cou[$coui] eq 1){
                                $rank="<font color=red size=4><b>★$cont_cou[$coui]位</b></font>";
                                $sort_value="<font color=red size=4><b>$sort_value</b></font>";
                        }
                        elsif($cont_cou[$coui] < 4){
                                $rank="<font color=blue size=3><b>$cont_cou[$coui]位</b></font>";
                                $sort_value="<font color=blue size=3><b>$sort_value</b></font>";
                        }
                        $con_table[$coui].="<tr><td bgcolor=$ELE_C[$con_ele[0]] size=2>$rank</td><td bgcolor=$ELE_C[$con_ele[0]] size=2>$ext_tl_name</td><td bgcolor=$ELE_C[$con_ele[0]]><img width=35 height=35 src=\"$IMG/chara/$ext_tl_chara.gif\"></td><td bgcolor=$ELE_C[$con_ele[0]]>$sort_value</td></tr>";
                }else{last;}
        }
        $coui++;
        foreach(@CL_DATA3){
                ($ext_tl_chara,$ext_tl_name,$ext_tl_month,$ext_tl_type[0],$ext_tl_type[1],$ext_tl_type[2],$ext_tl_type[3],$ext_tl_type[4],$ext_tl_type[5],$ext_tl_king,$ext_tl_lose,$ext_tl_lvup,$ext_tl_total,$ext_tl_gift,$ext_tl_mix,$ext_tl_rshop,$ext_tl_goditem,$ext_tl_nolucky) = split(/<>/);

                if($cont_cou[$coui]<10){
                        $cont_cou[$coui]++;
                        $rank="$cont_cou[$coui]位";
                        $sort_value=$ext_tl_rshop;
                        if($cont_cou[$coui] eq 1){
                                $rank="<font color=red size=4><b>★$cont_cou[$coui]位</b></font>";
                                $sort_value="<font color=red size=4><b>$sort_value</b></font>";
                        }
                        elsif($cont_cou[$coui] < 4){
                                $rank="<font color=blue size=3><b>$cont_cou[$coui]位</b></font>";
                                $sort_value="<font color=blue size=3><b>$sort_value</b></font>";
                        }
                        $con_table[$coui].="<tr><td bgcolor=$ELE_C[$con_ele[0]] size=2>$rank</td><td bgcolor=$ELE_C[$con_ele[0]] size=2>$ext_tl_name</td><td bgcolor=$ELE_C[$con_ele[0]]><img width=35 height=35 src=\"$IMG/chara/$ext_tl_chara.gif\"></td><td bgcolor=$ELE_C[$con_ele[0]]>$sort_value</td></tr>";
                }else{last;}
        }
        $coui++;
        foreach(@CL_DATA4){
                ($ext_tl_chara,$ext_tl_name,$ext_tl_month,$ext_tl_type[0],$ext_tl_type[1],$ext_tl_type[2],$ext_tl_type[3],$ext_tl_type[4],$ext_tl_type[5],$ext_tl_king,$ext_tl_lose,$ext_tl_lvup,$ext_tl_total,$ext_tl_gift,$ext_tl_mix,$ext_tl_rshop,$ext_tl_goditem,$ext_tl_nolucky) = split(/<>/);

                if($cont_cou[$coui]<10){
                        $cont_cou[$coui]++;
                        $rank="$cont_cou[$coui]位";
                        $sort_value=$ext_tl_goditem;
                        if($cont_cou[$coui] eq 1){
                                $rank="<font color=red size=4><b>★$cont_cou[$coui]位</b></font>";
                                $sort_value="<font color=red size=4><b>$sort_value</b></font>";
                        }
                        elsif($cont_cou[$coui] < 4){
                                $rank="<font color=blue size=3><b>$cont_cou[$coui]位</b></font>";
                                $sort_value="<font color=blue size=3><b>$sort_value</b></font>";
                        }
                        $con_table[$coui].="<tr><td bgcolor=$ELE_C[$con_ele[0]] size=2>$rank</td><td bgcolor=$ELE_C[$con_ele[0]] size=2>$ext_tl_name</td><td bgcolor=$ELE_C[$con_ele[0]]><img width=35 height=35 src=\"$IMG/chara/$ext_tl_chara.gif\"></td><td bgcolor=$ELE_C[$con_ele[0]]>$sort_value</td></tr>";
                }else{last;}
        }
        $coui++;
        foreach(@CL_DATA5){
                ($ext_tl_chara,$ext_tl_name,$ext_tl_month,$ext_tl_type[0],$ext_tl_type[1],$ext_tl_type[2],$ext_tl_type[3],$ext_tl_type[4],$ext_tl_type[5],$ext_tl_king,$ext_tl_lose,$ext_tl_lvup,$ext_tl_total,$ext_tl_gift,$ext_tl_mix,$ext_tl_rshop,$ext_tl_goditem,$ext_tl_nolucky) = split(/<>/);

                if($cont_cou[$coui]<10){
                        $cont_cou[$coui]++;
                        $rank="$cont_cou[$coui]位";
                        $sort_value="很倒楣";
                        if($cont_cou[$coui] eq 1){
                                $rank="<font color=red size=4><b>★$cont_cou[$coui]位</b></font>";
                                $sort_value="<font color=red size=4><b>超倒楣</b></font>";
                        }
                        elsif($cont_cou[$coui] < 4){
                                $rank="<font color=blue size=3><b>$cont_cou[$coui]位</b></font>";
                                $sort_value="<font color=blue size=3><b>非常倒楣</b></font>";
                        }
                        $con_table[$coui].="<tr><td bgcolor=$ELE_C[$con_ele[0]] size=2>$rank</td><td bgcolor=$ELE_C[$con_ele[0]] size=2>$ext_tl_name</td><td bgcolor=$ELE_C[$con_ele[0]]><img width=35 height=35 src=\"$IMG/chara/$ext_tl_chara.gif\"></td><td bgcolor=$ELE_C[$con_ele[0]]>$sort_value</td></tr>";
                }else{last;}
        }
        $coui++;
        foreach(@CL_DATA6){
                ($ext_tl_chara,$ext_tl_name,$ext_tl_month,$ext_tl_type[0],$ext_tl_type[1],$ext_tl_type[2],$ext_tl_type[3],$ext_tl_type[4],$ext_tl_type[5],$ext_tl_king,$ext_tl_lose,$ext_tl_lvup,$ext_tl_total,$ext_tl_gift,$ext_tl_mix,$ext_tl_rshop,$ext_tl_goditem,$ext_tl_nolucky) = split(/<>/);

                if($cont_cou[$coui]<10){
                        $cont_cou[$coui]++;
                        $rank="$cont_cou[$coui]位";
                        $sort_value=$ext_tl_total;
                        if($cont_cou[$coui] eq 1){
                                $rank="<font color=red size=4><b>★$cont_cou[$coui]位</b></font>";
                                $sort_value="<font color=red size=4><b>$sort_value</b></font>";
                        }
                        elsif($cont_cou[$coui] < 4){
                                $rank="<font color=blue size=3><b>$cont_cou[$coui]位</b></font>";
                                $sort_value="<font color=blue size=3><b>$sort_value</b></font>";
                        }
                        $con_table[$coui].="<tr><td bgcolor=$ELE_C[$con_ele[0]] size=2>$rank</td><td bgcolor=$ELE_C[$con_ele[0]] size=2>$ext_tl_name</td><td bgcolor=$ELE_C[$con_ele[0]]><img width=35 height=35 src=\"$IMG/chara/$ext_tl_chara.gif\"></td><td bgcolor=$ELE_C[$con_ele[0]]>$sort_value</td></tr>";
                }else{last;}
        }
        $coui++;
        foreach(@CL_DATA7){
                ($ext_tl_chara,$ext_tl_name,$ext_tl_month,$ext_tl_type[0],$ext_tl_type[1],$ext_tl_type[2],$ext_tl_type[3],$ext_tl_type[4],$ext_tl_type[5],$ext_tl_king,$ext_tl_lose,$ext_tl_lvup,$ext_tl_total,$ext_tl_gift,$ext_tl_mix,$ext_tl_rshop,$ext_tl_goditem,$ext_tl_nolucky) = split(/<>/);

                if($cont_cou[$coui]<10){
                        $cont_cou[$coui]++;
                        $rank="$cont_cou[$coui]位";
                        $sort_value=$ext_tl_king;
                        if($cont_cou[$coui] eq 1){
                                $rank="<font color=red size=4><b>★$cont_cou[$coui]位</b></font>";
                                $sort_value="<font color=red size=4><b>$sort_value</b></font>";
                        }
                        elsif($cont_cou[$coui] < 4){
                                $rank="<font color=blue size=3><b>$cont_cou[$coui]位</b></font>";
                                $sort_value="<font color=blue size=3><b>$sort_value</b></font>";
                        }
                        $con_table[$coui].="<tr><td bgcolor=$ELE_C[$con_ele[0]] size=2>$rank</td><td bgcolor=$ELE_C[$con_ele[0]] size=2>$ext_tl_name</td><td bgcolor=$ELE_C[$con_ele[0]]><img width=35 height=35 src=\"$IMG/chara/$ext_tl_chara.gif\"></td><td bgcolor=$ELE_C[$con_ele[0]]>$sort_value</td></tr>";
                }else{last;}
        }
        $coui++;
        foreach(@CL_DATA8){
                ($ext_tl_chara,$ext_tl_name,$ext_tl_month,$ext_tl_type[0],$ext_tl_type[1],$ext_tl_type[2],$ext_tl_type[3],$ext_tl_type[4],$ext_tl_type[5],$ext_tl_king,$ext_tl_lose,$ext_tl_lvup,$ext_tl_total,$ext_tl_gift,$ext_tl_mix,$ext_tl_rshop,$ext_tl_goditem,$ext_tl_nolucky) = split(/<>/);

                if($cont_cou[$coui]<10){
                        $cont_cou[$coui]++;
                        $rank="$cont_cou[$coui]位";
                        $sort_value=$ext_tl_lvup;
                        if($cont_cou[$coui] eq 1){
                                $rank="<font color=red size=4><b>★$cont_cou[$coui]位</b></font>";
                                $sort_value="<font color=red size=4><b>$sort_value</b></font>";
                        }
                        elsif($cont_cou[$coui] < 4){
                                $rank="<font color=blue size=3><b>$cont_cou[$coui]位</b></font>";
                                $sort_value="<font color=blue size=3><b>$sort_value</b></font>";
                        }
                        $con_table[$coui].="<tr><td bgcolor=$ELE_C[$con_ele[0]] size=2>$rank</td><td bgcolor=$ELE_C[$con_ele[0]] size=2>$ext_tl_name</td><td bgcolor=$ELE_C[$con_ele[0]]><img width=35 height=35 src=\"$IMG/chara/$ext_tl_chara.gif\"></td><td bgcolor=$ELE_C[$con_ele[0]]>$sort_value</td></tr>";
                }else{last;}
        }
        $coui++;
        foreach(@CL_DATA9){
                ($ext_tl_chara,$ext_tl_name,$ext_tl_month,$ext_tl_type[0],$ext_tl_type[1],$ext_tl_type[2],$ext_tl_type[3],$ext_tl_type[4],$ext_tl_type[5],$ext_tl_king,$ext_tl_lose,$ext_tl_lvup,$ext_tl_total,$ext_tl_gift,$ext_tl_mix,$ext_tl_rshop,$ext_tl_goditem,$ext_tl_nolucky) = split(/<>/);

                if($cont_cou[$coui]<10){
                        $cont_cou[$coui]++;
                        $rank="$cont_cou[$coui]位";
                        $sort_value=$ext_tl_lose;
                        if($cont_cou[$coui] eq 1){
                                $rank="<font color=red size=4><b>★$cont_cou[$coui]位</b></font>";
                                $sort_value="<font color=red size=4><b>$sort_value</b></font>";
                        }
                        elsif($cont_cou[$coui] < 4){
                                $rank="<font color=blue size=3><b>$cont_cou[$coui]位</b></font>";
                                $sort_value="<font color=blue size=3><b>$sort_value</b></font>";
                        }
                        $con_table[$coui].="<tr><td bgcolor=$ELE_C[$con_ele[0]] size=2>$rank</td><td bgcolor=$ELE_C[$con_ele[0]] size=2>$ext_tl_name</td><td bgcolor=$ELE_C[$con_ele[0]]><img width=35 height=35 src=\"$IMG/chara/$ext_tl_chara.gif\"></td><td bgcolor=$ELE_C[$con_ele[0]]>$sort_value</td></tr>";
                }else{last;}
        }
        $coui++;
        foreach(@CL_DATA10){
                ($ext_tl_chara,$ext_tl_name,$ext_tl_month,$ext_tl_type[0],$ext_tl_type[1],$ext_tl_type[2],$ext_tl_type[3],$ext_tl_type[4],$ext_tl_type[5],$ext_tl_king,$ext_tl_lose,$ext_tl_lvup,$ext_tl_total,$ext_tl_gift,$ext_tl_mix,$ext_tl_rshop,$ext_tl_goditem,$ext_tl_nolucky) = split(/<>/);

                if($cont_cou[$coui]<10){
                        $cont_cou[$coui]++;
                        $rank="$cont_cou[$coui]位";
                        $sort_value=$ext_tl_type[0];
                        if($cont_cou[$coui] eq 1){
                                $rank="<font color=red size=4><b>★$cont_cou[$coui]位</b></font>";
                                $sort_value="<font color=red size=4><b>$sort_value</b></font>";
                        }
                        elsif($cont_cou[$coui] < 4){
                                $rank="<font color=blue size=3><b>$cont_cou[$coui]位</b></font>";
                                $sort_value="<font color=blue size=3><b>$sort_value</b></font>";
                        }
                        $con_table[$coui].="<tr><td bgcolor=$ELE_C[$con_ele[0]] size=2>$rank</td><td bgcolor=$ELE_C[$con_ele[0]] size=2>$ext_tl_name</td><td bgcolor=$ELE_C[$con_ele[0]]><img width=35 height=35 src=\"$IMG/chara/$ext_tl_chara.gif\"></td><td bgcolor=$ELE_C[$con_ele[0]]>$sort_value</td></tr>";
                }else{last;}
        }

        $coui++;
        foreach(@CL_DATA11){
                ($ext_tl_chara,$ext_tl_name,$ext_tl_month,$ext_tl_type[0],$ext_tl_type[1],$ext_tl_type[2],$ext_tl_type[3],$ext_tl_type[4],$ext_tl_type[5],$ext_tl_king,$ext_tl_lose,$ext_tl_lvup,$ext_tl_total,$ext_tl_gift,$ext_tl_mix,$ext_tl_rshop,$ext_tl_goditem,$ext_tl_nolucky) = split(/<>/);

                if($cont_cou[$coui]<10){
                        $cont_cou[$coui]++;
                        $rank="$cont_cou[$coui]位";
                        $sort_value=$ext_tl_type[1];
                        if($cont_cou[$coui] eq 1){
                                $rank="<font color=red size=4><b>★$cont_cou[$coui]位</b></font>";
                                $sort_value="<font color=red size=4><b>$sort_value</b></font>";
                        }
                        elsif($cont_cou[$coui] < 4){
                                $rank="<font color=blue size=3><b>$cont_cou[$coui]位</b></font>";
                                $sort_value="<font color=blue size=3><b>$sort_value</b></font>";
                        }
                        $con_table[$coui].="<tr><td bgcolor=$ELE_C[$con_ele[0]] size=2>$rank</td><td bgcolor=$ELE_C[$con_ele[0]] size=2>$ext_tl_name</td><td bgcolor=$ELE_C[$con_ele[0]]><img width=35 height=35 src=\"$IMG/chara/$ext_tl_chara.gif\"></td><td bgcolor=$ELE_C[$con_ele[0]]>$sort_value</td></tr>";
                }else{last;}
        }

        $coui++;
        foreach(@CL_DATA12){
                ($ext_tl_chara,$ext_tl_name,$ext_tl_month,$ext_tl_type[0],$ext_tl_type[1],$ext_tl_type[2],$ext_tl_type[3],$ext_tl_type[4],$ext_tl_type[5],$ext_tl_king,$ext_tl_lose,$ext_tl_lvup,$ext_tl_total,$ext_tl_gift,$ext_tl_mix,$ext_tl_rshop,$ext_tl_goditem,$ext_tl_nolucky) = split(/<>/);

                if($cont_cou[$coui]<10){
                        $cont_cou[$coui]++;
                        $rank="$cont_cou[$coui]位";
                        $sort_value=$ext_tl_type[2];
                        if($cont_cou[$coui] eq 1){
                                $rank="<font color=red size=4><b>★$cont_cou[$coui]位</b></font>";
                                $sort_value="<font color=red size=4><b>$sort_value</b></font>";
                        }
                        elsif($cont_cou[$coui] < 4){
                                $rank="<font color=blue size=3><b>$cont_cou[$coui]位</b></font>";
                                $sort_value="<font color=blue size=3><b>$sort_value</b></font>";
                        }
                        $con_table[$coui].="<tr><td bgcolor=$ELE_C[$con_ele[0]] size=2>$rank</td><td bgcolor=$ELE_C[$con_ele[0]] size=2>$ext_tl_name</td><td bgcolor=$ELE_C[$con_ele[0]]><img width=35 height=35 src=\"$IMG/chara/$ext_tl_chara.gif\"></td><td bgcolor=$ELE_C[$con_ele[0]]>$sort_value</td></tr>";
                }else{last;}
        }
        $coui++;
        foreach(@CL_DATA13){
                ($ext_tl_chara,$ext_tl_name,$ext_tl_month,$ext_tl_type[0],$ext_tl_type[1],$ext_tl_type[2],$ext_tl_type[3],$ext_tl_type[4],$ext_tl_type[5],$ext_tl_king,$ext_tl_lose,$ext_tl_lvup,$ext_tl_total,$ext_tl_gift,$ext_tl_mix,$ext_tl_rshop,$ext_tl_goditem,$ext_tl_nolucky) = split(/<>/);

                if($cont_cou[$coui]<10){
                        $cont_cou[$coui]++;
                        $rank="$cont_cou[$coui]位";
                        $sort_value=$ext_tl_type[3];
                        if($cont_cou[$coui] eq 1){
                                $rank="<font color=red size=4><b>★$cont_cou[$coui]位</b></font>";
                                $sort_value="<font color=red size=4><b>$sort_value</b></font>";
                        }
                        elsif($cont_cou[$coui] < 4){
                                $rank="<font color=blue size=3><b>$cont_cou[$coui]位</b></font>";
                                $sort_value="<font color=blue size=3><b>$sort_value</b></font>";
                        }
                        $con_table[$coui].="<tr><td bgcolor=$ELE_C[$con_ele[0]] size=2>$rank</td><td bgcolor=$ELE_C[$con_ele[0]] size=2>$ext_tl_name</td><td bgcolor=$ELE_C[$con_ele[0]]><img width=35 height=35 src=\"$IMG/chara/$ext_tl_chara.gif\"></td><td bgcolor=$ELE_C[$con_ele[0]]>$sort_value</td></tr>";
                }else{last;}
        }
        $coui++;
        foreach(@CL_DATA14){
                ($ext_tl_chara,$ext_tl_name,$ext_tl_month,$ext_tl_type[0],$ext_tl_type[1],$ext_tl_type[2],$ext_tl_type[3],$ext_tl_type[4],$ext_tl_type[5],$ext_tl_king,$ext_tl_lose,$ext_tl_lvup,$ext_tl_total,$ext_tl_gift,$ext_tl_mix,$ext_tl_rshop,$ext_tl_goditem,$ext_tl_nolucky) = split(/<>/);

                if($cont_cou[$coui]<10){
                        $cont_cou[$coui]++;
                        $rank="$cont_cou[$coui]位";
                        $sort_value=$ext_tl_type[4];
                        if($cont_cou[$coui] eq 1){
                                $rank="<font color=red size=4><b>★$cont_cou[$coui]位</b></font>";
                                $sort_value="<font color=red size=4><b>$sort_value</b></font>";
                        }
                        elsif($cont_cou[$coui] < 4){
                                $rank="<font color=blue size=3><b>$cont_cou[$coui]位</b></font>";
                                $sort_value="<font color=blue size=3><b>$sort_value</b></font>";
                        }
                        $con_table[$coui].="<tr><td bgcolor=$ELE_C[$con_ele[0]] size=2>$rank</td><td bgcolor=$ELE_C[$con_ele[0]] size=2>$ext_tl_name</td><td bgcolor=$ELE_C[$con_ele[0]]><img width=35 height=35 src=\"$IMG/chara/$ext_tl_chara.gif\"></td><td bgcolor=$ELE_C[$con_ele[0]]>$sort_value</td></tr>";
                }else{last;}
        }

        $coui++;
        foreach(@CL_DATA15){
                ($ext_tl_chara,$ext_tl_name,$ext_tl_month,$ext_tl_type[0],$ext_tl_type[1],$ext_tl_type[2],$ext_tl_type[3],$ext_tl_type[4],$ext_tl_type[5],$ext_tl_king,$ext_tl_lose,$ext_tl_lvup,$ext_tl_total,$ext_tl_gift,$ext_tl_mix,$ext_tl_rshop,$ext_tl_goditem,$ext_tl_nolucky) = split(/<>/);

                if($cont_cou[$coui]<10){
                        $cont_cou[$coui]++;
                        $rank="$cont_cou[$coui]位";
                        $sort_value=$ext_tl_type[5];
                        if($cont_cou[$coui] eq 1){
                                $rank="<font color=red size=4><b>★$cont_cou[$coui]位</b></font>";
                                $sort_value="<font color=red size=4><b>$sort_value</b></font>";
                        }
                        elsif($cont_cou[$coui] < 4){
                                $rank="<font color=blue size=3><b>$cont_cou[$coui]位</b></font>";
                                $sort_value="<font color=blue size=3><b>$sort_value</b></font>";
                        }
                        $con_table[$coui].="<tr><td bgcolor=$ELE_C[$con_ele[0]] size=2>$rank</td><td bgcolor=$ELE_C[$con_ele[0]] size=2>$ext_tl_name</td><td bgcolor=$ELE_C[$con_ele[0]]><img width=35 height=35 src=\"$IMG/chara/$ext_tl_chara.gif\"></td><td bgcolor=$ELE_C[$con_ele[0]]>$sort_value</td></tr>";
                }else{last;}
        }


        $con_no=0;
        for($i=0;$i<15;$i++){
                $con_table[$i].="</table>";
        }
        print"<table colspan=5>";
        for($i=0;$i<15;$i++){
                if($i%5 eq 0){
                        print"<tr><td>$con_table[$i]</td>";
                }elsif($i eq 4 || $i eq 9 || $i eq 14){
                        print"<td>$con_table[$i]</td></tr>";
                }else{
                        print"<td>$con_table[$i]</td>";
                }
        }
        print"</table>";
        print"<center><font color=yellow>遊戲人數：$mn名</font></center><BR>";
&mainfooter;
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
exit;

