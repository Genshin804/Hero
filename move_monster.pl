	$tt = time ;
        ($sec,$min,$hour,$mday,$mon,$year,$wday,$yday) = localtime(time);
        $year += 1900;
        $mon++;
        $ww = (Sun,Mon,Tue,Wed,Thu,Fri,Sat)[$wday];
        $daytime = sprintf("%4d\/%02d\/%02d\/(%s)　%02d時%02d分", $year,$mon,$mday,$ww,$hour,$min);
        open(IN,"/var/www/hero/data/townmonster.cgi");
	@mdata = <IN>;
	close(IN);
        ($ename,$eab,$etec,$esk,$e_ex,$e_gold,$etown,$elv)=split(/<>/,$mdata[0]);
        ($ehp,$emp,$str,$vit,$eint,$efai,$edex,$eagi,$eele)=split(/,/,$eab);
	if ($ehp ne"0"){
		open(IN,"/var/www/hero/data/towndata.cgi");
	        @TOWN_DATA = <IN>;
        	close(IN);

	        $t_no = 0;
	        $tx=0;
	        $movtown[0]=$etown;
	        foreach(@TOWN_DATA){
	                ($town_id,$town_name,$town_con,$town_ele,$town_gold,$town_arm,$town_pro,$town_acc,$town_ind,$town_tr,$town_s,$town_x,$town_y,$town_build,$town_etc)=split(/<>/);
	                if($etown eq "$town_id"){
	                		$town2_x=$town_x;
	                		$town2_y=$town_y;
	                        $last;
	                }
	                $t_no++;
	        }
	        $t_no = 0;
	        foreach(@TOWN_DATA){
	                ($town_id,$town_name,$town_con,$town_ele,$town_gold,$town_arm,$town_pro,$town_acc,$town_ind,$town_tr,$town_s,$town_x,$town_y,$town_build,$town_etc)=split(/<>/);
	                if(abs($town2_x-$town_x) <= "1" && abs($town2_y-$town_y) <= "1"){
				$tx++;
	                        $movtown[$tx]=$town_id;
				$movcon[$tx]=$town_con;
	                }
	                $t_no++;
	        }
		$tx++;
		$movidx=int(rand($tx));
		$town=$movtown[$movidx];
		$town_con=$movcon[$movidx]+0;
                if($town >22){$town=0;$town_con=0;}

		$ehp+=int(rand(5000))+5000;
		if($ehp>100000){
			$ehp=100000;
		}
		if($etown ne $town){
        open(IN,"/var/www/hero/data/country.cgi");
        @CON_DATA = <IN>;
        close(IN);

        $c_no = 0;
        foreach(@CON_DATA){
                ($con_id,$con_name,$con_ele,$con_gold,$con_king,$con_yaku,$con_cou,$con_mes,$con_etc)=split(/<>/);
                if("$con_id" eq "$town_con"){$hit=1;last;}
        }
        if(!$hit){
                $con_id=0;$con_name="無所屬";
        }


	                $mdata[0]="$ename<>$eab<>$etec<>$esk<>$e_ex<>$e_gold<>$town<>$elv";
                	open (OUT, "> /var/www/hero/data/townmonster.cgi");
        	        print OUT @mdata;
	                close (OUT);

	        	open(IN,"/var/www/hero/data/maplog.cgi");
		        @data = <IN>;
	        	close(IN);
	        	unshift(@data, "<font color=red><b>[神獸]</b>神獸移動到「$con_name國」的某個城鎮。</font>($daytime)\n");
	        	splice(@data,10);
		        open (OUT, "> /var/www/hero/data/maplog.cgi");
		        print OUT @data;
		        open (OUT, "> /var/www/data/maplogtime.cgi");
		        print OUT $tt;
		        close (OUT);

		}
	}

