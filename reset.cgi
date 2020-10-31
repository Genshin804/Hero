##############
# Reset Mode #
##############

sub RESET_MODE{

	# MAIN DATA
	$dir="./logfile/chara";
	opendir(dirlist,"$dir");
	while($file = readdir(dirlist)){
		if($file =~ /\.cgi/i){
			unlink("$dir/$file");
		}
	}
	closedir(dirlist);

	# HISTORY DATA
	$dir="./logfile/history";
	opendir(dirlist,"$dir");
	while($file = readdir(dirlist)){
		if($file =~ /\.cgi/i){
			unlink("$dir/$file");
		}
	}
	closedir(dirlist);

	# ITEM DATA
	$dir="./logfile/item";
	opendir(dirlist,"$dir");
	while($file = readdir(dirlist)){
		if($file =~ /\.cgi/i){
			unlink("$dir/$file");
		}
	}
	closedir(dirlist);

	# STORAGE DATA
	$dir="./logfile/storage";
	opendir(dirlist,"$dir");
	while($file = readdir(dirlist)){
		if($file =~ /\.cgi/i){
			unlink("$dir/$file");
		}
	}
	closedir(dirlist);

	# JOB DATA
	$dir="./logfile/job";
	opendir(dirlist,"$dir");
	while($file = readdir(dirlist)){
		if($file =~ /\.cgi/i){
			unlink("$dir/$file");
		}
	}
	closedir(dirlist);

	# ABILITY DATA
	$dir="./logfile/ability";
	opendir(dirlist,"$dir");
	while($file = readdir(dirlist)){
		if($file =~ /\.cgi/i){
			unlink("$dir/$file");
		}
	}
	closedir(dirlist);

	# OUT DATA
	$dir="./logfile/out";
	opendir(dirlist,"$dir");
	while($file = readdir(dirlist)){
		if($file =~ /\.cgi/i){
			unlink("$dir/$file");
		}
	}
	closedir(dirlist);

	# MESS DATA
	$dir="./logfile/mes";
	opendir(dirlist,"$dir");
	while($file = readdir(dirlist)){
		if($file =~ /\.cgi/i){
			unlink("$dir/$file");
		}
	}
	closedir(dirlist);

	# PROF DATA
	$dir="./logfile/prof";
	opendir(dirlist,"$dir");
	while($file = readdir(dirlist)){
		if($file =~ /\.cgi/i){
			unlink("$dir/$file");
		}
	}
	closedir(dirlist);

	# meslog
	$dir="./meslog";
	opendir(dirlist,"$dir");
	while($file = readdir(dirlist)){
		if($file =~ /\.cgi/i){
			unlink("$dir/$file");
		}
	}
	closedir(dirlist);

	# chat
	$dir="./blog/chat";
	opendir(dirlist,"$dir");
	while($file = readdir(dirlist)){
		if($file =~ /\.cgi/i){
			unlink("$dir/$file");
		}
	}
	closedir(dirlist);

	# conv
	$dir="./blog/conv";
	opendir(dirlist,"$dir");
	while($file = readdir(dirlist)){
		if($file =~ /\.cgi/i){
			unlink("$dir/$file");
		}
	}
	closedir(dirlist);

	# rule
	$dir="./blog/rule";
	opendir(dirlist,"$dir");
	while($file = readdir(dirlist)){
		if($file =~ /\.cgi/i){
			unlink("$dir/$file");
		}
	}
	closedir(dirlist);
	

	# NEW DATA
	@NEW_DATA = ();

	# COUNTRY
	$confile = "./data/country.cgi";
	open(OUT,">$confile");
	print OUT @NEW_DATA;
	close(OUT);

	# TOWNDATA
	open(IN,"./data/towndatabk.cgi") or &error("檔案開啟錯誤：reset.cgi(138)。");
	@TOWN_DATA = <IN>;
	close(IN);

	$confile = "./data/towndata.cgi";
	open(OUT,">$confile");
	print OUT @TOWN_DATA;
	close(OUT);

	# BUILD LIST
	open(OUT,">./data/build.cgi");
	print OUT @NEW_DATA;
	close(OUT);

	# CARM LIST
	open(OUT,">./data/carm.cgi");
	print OUT @NEW_DATA;
	close(OUT);

	# DEF LIST
	open(OUT,">./data/def.cgi");
	print OUT @NEW_DATA;
	close(OUT);

	# ENTRY LIST
	open(OUT,">./data/entry_list.cgi");
	print OUT @NEW_DATA;
	close(OUT);

	# GUEST LIST
	open(OUT,">./data/guest_list.cgi");
	print OUT @NEW_DATA;
	close(OUT);

	# MAP LOG LIST
	open(OUT,">./data/maplog.cgi");
	print OUT @NEW_DATA;
	close(OUT);

	# MAP LOG LIST2
	open(OUT,">./data/maplog2.cgi");
	print OUT @NEW_DATA;
	close(OUT);

	# MAP LOG LIST3
	open(OUT,">./data/maplog3.cgi");
	print OUT @NEW_DATA;
	close(OUT);

	# MAP LOG LIST4
	open(OUT,">./data/maplog4.cgi");
	print OUT @NEW_DATA;
	close(OUT);

	# MAP LOG LIST5
	open(OUT,">./data/maplog5.cgi");
	print OUT @NEW_DATA;
	close(OUT);

	# MAP LOG LIST6
	open(OUT,">./data/maplog6.cgi");
	print OUT @NEW_DATA;
	close(OUT);

	# MAP LOG LIST6
	open(OUT,">./data/maplog7.cgi");
	print OUT @NEW_DATA;
	close(OUT);

	# UNIT LIST
	open(OUT,">./data/unit.cgi");
	print OUT @NEW_DATA;
	close(OUT);

	
	&maplog("所有資料初始化。");
}
sub RESET_MODE2{

	# chat
	$dir="./blog/chat";
	opendir(dirlist,"$dir");
	while($file = readdir(dirlist)){
		if($file =~ /\.cgi/i){
			unlink("$dir/$file");
		}
	}
	closedir(dirlist);

	# conv
	$dir="./blog/conv";
	opendir(dirlist,"$dir");
	while($file = readdir(dirlist)){
		if($file =~ /\.cgi/i){
			unlink("$dir/$file");
		}
	}
	closedir(dirlist);

	# rule
	$dir="./blog/rule";
	opendir(dirlist,"$dir");
	while($file = readdir(dirlist)){
		if($file =~ /\.cgi/i){
			unlink("$dir/$file");
		}
	}
	closedir(dirlist);
	

	# NEW DATA
	@NEW_DATA = ();

	# COUNTRY
	$confile = "./data/country.cgi";
	open(OUT,">$confile");
	print OUT @NEW_DATA;
	close(OUT);

	# TOWN
	open(IN,"./data/towndatabk.cgi") or &error("資料開啟錯誤：reset.cgi(263)。");
	@TOWN_DATA = <IN>;
	close(IN);

	$confile = "./data/towndata.cgi";
	open(OUT,">$confile");
	print OUT @TOWN_DATA;
	close(OUT);

	# BUILD LIST
	open(OUT,">./data/build.cgi");
	print OUT @NEW_DATA;
	close(OUT);

	# CARM
	open(OUT,">./data/carm.cgi");
	print OUT @NEW_DATA;
	close(OUT);

	# DEF LIST
	open(OUT,">./data/def.cgi");
	print OUT @NEW_DATA;
	close(OUT);

	# FREE LIST
	open(OUT,">./data/free.cgi");
	print OUT @NEW_DATA;
	close(OUT);

	# ENTRY LIST
	open(OUT,">./data/entry_list.cgi");
	print OUT @NEW_DATA;
	close(OUT);

	# GUEST LIST
	open(OUT,">./data/guest_list.cgi");
	print OUT @NEW_DATA;
	close(OUT);

	# MAP LOG LIST
	open(OUT,">./data/maplog.cgi");
	print OUT @NEW_DATA;
	close(OUT);

	# MAP LOG LIST2
	open(OUT,">./data/maplog2.cgi");
	print OUT @NEW_DATA;
	close(OUT);

	# MAP LOG LIST3
	open(OUT,">./data/maplog3.cgi");
	print OUT @NEW_DATA;
	close(OUT);

	# MAP LOG LIST4
	open(OUT,">./data/maplog4.cgi");
	print OUT @NEW_DATA;
	close(OUT);

	# MAP LOG LIST5
	open(OUT,">./data/maplog5.cgi");
	print OUT @NEW_DATA;
	close(OUT);

	# MAP LOG LIST6
	open(OUT,">./data/maplog6.cgi");
	print OUT @NEW_DATA;
	close(OUT);

	# MAP LOG LIST6
	open(OUT,">./data/maplog7.cgi");
	print OUT @NEW_DATA;
	close(OUT);

	# WINNER LIST
	open(OUT,">./data/winner_list.cgi");
	print OUT @NEW_DATA;
	close(OUT);

	&maplog("系統資料初始化。");
}
1;

