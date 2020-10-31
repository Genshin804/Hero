#! /usr/bin/perl
require './jcode.pl';
require './sub.cgi';
require './conf.cgi';
require './conf_eq.cgi';
require './conf_pet.cgi';
require './battle_suport.cgi';

&decode;
if($ENV{'HTTP_REFERER'} !~ /cgi$/ ){ &error2("<a href='./login.cgi'>請重新登入</a>。"); }
if ($in{'id'} eq "2930"){
        &verchklog("town.cgi,$in{'mode'}");
}
if($in{'mode'} eq "battle2"){require './battle/battle2.pl';&battle2;}
elsif($in{'mode'} eq "giveup2"){require './battle/giveup2.pl';&giveup2;}
elsif($in{'mode'} eq "kunren"){require './battle/kunren.pl';&kunren;}
elsif($in{'mode'} eq "kunren2"){require './battle/kunren2.pl';&kunren2;}
elsif($in{'mode'} eq "toubatsu"){require './battle/toubatsu.pl';&toubatsu;}
elsif($in{'mode'} eq "toubatsu2"){require './battle/toubatsu2.pl';&toubatsu2;}
elsif($in{'mode'} eq "townmonster"){require './battle/townmonster.pl';&townmonster;}
elsif($in{'mode'}){require './battle/battle.pl';&bat;}
else{&error2("傳送資料有誤。");}
exit;

