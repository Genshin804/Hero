package jcode; 
;###################################################################### 
;# 
;# jcode.pl: Perl library for Japanese character code conversion 
;# 
;# Copyright (c) 1995-1999 Kazumasa Utashiro <utashiro@iij.ad.jp> 
;# Internet Initiative Japan Inc. 
;# 3-13 Kanda Nishiki-cho, Chiyoda-ku, Tokyo 101-0054, Japan 
;# 
;# Copyright (c) 1992,1993,1994 Kazumasa Utashiro 
;# Software Research Associates, Inc. 
;# 
;# Original version was developed under the name of srekcah@sra.co.jp 
;# February 1992 and it was called kconv.pl at the beginning.  This 
;# address was a pen name for group of individuals and it is no longer 
;# valid. 
;# 
;# Use and redistribution for ANY PURPOSE, without significant 
;# modification, is granted as long as all copyright notices are 
;# retained.  THIS SOFTWARE IS PROVIDED BY THE AUTHOR ``AS IS'' AND 
;# ANY EXPRESS OR IMPLIED WARRANTIES ARE DISCLAIMED. 
;# 
;# The latest version is available here: 
;# 
;#    ftp://ftp.iij.ad.jp/pub/IIJ/dist/utashiro/perl/ 
;# 
;; $rcsid = q$Id: jcode.pl,v 2.10 1999/01/10 13:43:14 utashiro Exp $; 
;# 
;###################################################################### 
;# 
;# PERL4 INTERFACE: 
;# 
;#    &jcode'getcode(*line) 
;#        Return 'jis', 'sjis', 'euc' or undef according to 
;#        Japanese character code in $line.  Return 'binary' if 
;#        the data has non-character code. 
;# 
;#        When evaluated in array context, it returns a list 
;#        contains two items.  First value is the number of 
;#        characters which matched to the expected code, and 
;#        second value is the code name.  It is useful if and 
;#        only if the number is not 0 and the code is undef; 
;#        that case means it couldn't tell 'euc' or 'sjis' 
;#        because the evaluation score was exactly same.  This 
;#        interface is too tricky, though. 
;# 
;#        Code detection between euc and sjis is very difficult 
;#        or sometimes impossible or even lead to wrong result 
;#        when it includes JIS X0201 KANA characters.  So JIS 
;#        X0201 KANA is ignored for automatic code detection. 
;# 
;#    &jcode'convert(*line, $ocode [, $icode [, $option]]) 
;#        Convert the contents of $line to the specified 
;#        Japanese code given in the second argument $ocode. 
;#        $ocode can be any of "jis", "sjis" or "euc", or use 
;#        "noconv" when you don't want the code conversion. 
;#        Input code is recognized automatically from the line 
;#        itself when $icode is not supplied (JIS X0201 KANA is 
;#        ignored in code detection.  See the above descripton 
;#        of &getcode).  $icode also can be specified, but 
;#        xxx2yyy routine is more efficient when both codes are 
;#        known. 
;# 
;#        It returns the code of input string in scalar context, 
;#        and a list of pointer of convert subroutine and the 
;#        input code in array context. 
;# 
;#        Japanese character code JIS X0201, X0208, X0212 and 
;#        ASCII code are supported.  X0212 characters can not be 
;#        represented in SJIS and they will be replased by 
;#        "geta" character when converted to SJIS. 
;# 
;#        See next paragraph for $option parameter. 
;# 
;#    &jcode'xxx2yyy(*line [, $option]) 
;#        Convert the Japanese code from xxx to yyy.  String xxx 
;#        and yyy are any convination from "jis", "euc" or 
;#        "sjis".  They return *approximate* number of converted 
;#        bytes.  So return value 0 means the line was not 
;#        converted at all. 
;# 
;#        Optional parameter $option is used to specify optional 
;#        conversion method.  String "z" is for JIS X0201 KANA 
;#        to X0208 KANA, and "h" is for reverse. 
;# 
;#    $jcode'convf{'xxx', 'yyy'} 
;#        The value of this associative array is pointer to the 
;#        subroutine jcode'xxx2yyy(). 
;# 
;#    &jcode'to($ocode, $line [, $icode [, $option]]) 
;#    &jcode'jis($line [, $icode [, $option]]) 
;#    &jcode'euc($line [, $icode [, $option]]) 
;#    &jcode'sjis($line [, $icode [, $option]]) 
;#        These functions are prepared for easy use of 
;#        call/return-by-value interface.  You can use these 
;#        funcitons in s///e operation or any other place for 
;#        convenience. 
;# 
;#    &jcode'jis_inout($in, $out) 
;#        Set or inquire JIS start and end sequences.  Default 
;#        is "ESC-$-B" and "ESC-(-B".  If you supplied only one 
;#        character, "ESC-$" or "ESC-(" is prepended for each 
;#        character respectively.  Acutually "ESC-(-B" is not a 
;#        sequence to end JIS code but a sequence to start ASCII 
;#        code set.  So `in' and `out' are somewhat misleading. 
;# 
;#    &jcode'get_inout($string) 
;#        Get JIS start and end sequences from $string. 
;# 
;#    &jcode'cache() 
;#    &jcode'nocache() 
;#    &jcode'flush() 
;#        Usually, converted character is cached in memory to 
;#        avoid same calculations have to be done many times. 
;#        To disable this caching, call &jcode'nocache().  It 
;#        can be revived by &jcode'cache() and cache is flushed 
;#        by calling &jcode'flush().  &cache() and &nocache() 
;#        functions return previous caching state. 
;# 
;#    --------------------------------------------------------------- 
;# 
;#    &jcode'h2z_xxx(*line) 
;#        JIS X0201 KANA (so-called Hankaku-KANA) to X0208 KANA 
;#        (Zenkaku-KANA) code conversion routine.  String xxx is 
;#        any of "jis", "sjis" and "euc".  From the difficulty 
;#        of recognizing code set from 1-byte KATAKANA string, 
;#        automatic code recognition is not supported. 
;# 
;#    &jcode'z2h_xxx(*line) 
;#        X0208 to X0201 KANA code conversion routine.  String 
;#        xxx is any of "jis", "sjis" and "euc". 
;# 
;#    $jcode'z2hf{'xxx'} 
;#    $jcode'h2zf{'xxx'} 
;#        These are pointer to the corresponding function just 
;#        as $jcode'convf. 
;# 
;#    --------------------------------------------------------------- 
;# 
;#    &jcode'tr(*line, $from, $to [, $option]) 
;#        &jcode'tr emulates tr operator for 2 byte code.  Only 'd' 
;#        is interpreted as an option. 
;# 
;#        Range operator like `A-Z' for 2 byte code is partially 
;#        supported.  Code must be JIS or EUC, and first byte 
;#        have to be same on first and last character. 
;# 
;#        CAUTION: Handling range operator is a kind of trick 
;#        and it is not perfect.  So if you need to transfer `-' 
;#        character, please be sure to put it at the beginning 
;#        or the end of $from and $to strings. 
;# 
;#    &jcode'trans($line, $from, $to [, $option) 
;#        Same as &jcode'tr but accept string and return string 
;#        after translation. 
;# 
;#    --------------------------------------------------------------- 
;# 
;#    &jcode'init() 
;#        Initialize the variables used in this package.  You 
;#        don't have to call this when using jocde.pl by `do' or 
;#        `require' interface.  Call it first if you embedded 
;#        the jcode.pl at the end of your script. 
;# 
;###################################################################### 
;# 
;# PERL5 INTERFACE: 
;# 
;#    Current jcode.pl is written in Perl 4 but it is possible to 
;#    use from Perl 5 using `references'.  Fully perl5 capable version 
;#    is future issue. 
;# 
;#    jcode::getcode(\$line) 
;#    jcode::convert(\$line, $ocode [, $icode [, $option]]) 
;#    jcode::xxx2yyy(\$line [, $option]) 
;#    &{$jcode::convf{'xxx', 'yyy'}}(\$line) 
;#    jcode::to($ocode, $line [, $icode [, $option]]) 
;#    jcode::jis($line [, $icode [, $option]]) 
;#    jcode::euc($line [, $icode [, $option]]) 
;#    jcode::sjis($line [, $icode [, $option]]) 
;#    jcode::jis_inout($in, $out) 
;#    jcode::get_inout($string) 
;#    jcode::cache() 
;#    jcode::nocache() 
;#    jcode::flush() 
;#    jcode::h2z_xxx(\$line) 
;#    jcode::z2h_xxx(\$line) 
;#    &{$jcode::z2hf{'xxx'}}(\$line) 
;#    &{$jcode::h2zf{'xxx'}}(\$line) 
;#    jcode::tr(\$line, $from, $to [, $option]) 
;#    jcode::trans($line, $from, $to [, $option) 
;#    jcode::init() 
;# 
;###################################################################### 
;# 
;# SAMPLES 
;# 
;# Convert any Kanji code to JIS and print each line with code name. 
;# 
;#    while (<>) { 
;#        $code = &jcode'convert(*_, 'jis'); 
;#        print $code, "\t", $_; 
;#    } 
;#     
;# Convert all lines to JIS according to the first recognized line. 
;# 
;#    while (<>) { 
;#        print, next unless /[\033\200-\377]/; 
;#        (*f, $icode) = &jcode'convert(*_, 'jis'); 
;#        print; 
;#        defined(&f) || next; 
;#        while (<>) { &f(*_); print; } 
;#        last; 
;#    } 
;# 
;# The safest way of JIS conversion. 
;# 
;#    while (<>) { 
;#        ($matched, $code) = &jcode'getcode(*_); 
;#        print, next unless (@buf || $matched); 
;#        push(@buf, $_); 
;#        next unless $code; 
;#        eval "&jcode'${code}2jis(*_), print while (\$_ = shift(\@buf));"; 
;#        eval "&jcode'${code}2jis(*_), print while (\$_ = <>);"; 
;#        last; 
;#    } 
;#         
;###################################################################### 

;# 
;# Call initialize function if it is not called yet.  This may sound 
;# strange but it makes easy to embed the jcode.pl at the end of 
;# script.  Call &jcode'init at the beginning of the script in that 
;# case. 
;# 
&init unless defined $version; 
sub init { 
} 
sub jis_inout { 
} 
sub get_inout { 
} 
sub getcode { 
} 
sub max { 
} 
sub convert { 
} 
sub jis  { 
} 
sub euc  { 
} 
sub sjis { 
} 
sub to { 
} 
sub what { 
} 
sub trans { 
} 
sub sjis2jis { 
} 
sub _sjis2jis { 
} 
sub __sjis2jis { 
} 
sub euc2jis { 
} 
sub _euc2jis { 
} 
sub __euc2jis { 
} 
sub jis2euc { 
} 
sub _jis2euc { 
} 
sub jis2sjis { 
} 
sub _jis2sjis { 
} 
sub sjis2euc { 
} 
sub s2e { 
} 
sub euc2sjis { 
} 
sub e2s { 
} 
sub jis2jis { 
} 
sub sjis2sjis { 
} 
sub euc2euc { 
} 
sub cache { 
} 
sub nocache { 
} 
sub flushcache { 
} 
sub h2z_jis { 
} 
sub _h2z_jis { 
} 
sub h2z_euc { 
} 
sub h2z_sjis { 
} 
sub z2h_jis { 
} 
sub _z2h_jis { 
} 
sub __z2h_jis { 
} 
sub z2h_euc {
   local(*s, $n) = @_;
   &init_z2h_euc if !%z2h_euc;
   $s =~ s/($re_euc_c|$re_euc_kana)/$z2h_euc{$1} ? ($n++, $z2h_euc{$1}) : $1/geo;
   $n;
}
 
sub z2h_sjis {
   local(*s, $n) = @_;
   &init_z2h_sjis if !%z2h_sjis;
   $s =~ s/($re_sjis_c)/$z2h_sjis{$1} ? ($n++, $z2h_sjis{$1}) : $1/geo;
   $n;
}
sub init_z2h_euc { 
} 
sub init_z2h_sjis { 
} 
sub tr { 
} 
sub _maketable { 
} 
sub _expnd1 { 
} 
sub _expnd2 { 
} 

1; 
