#!/perl
use warnings;
use strict;
use diagnostics;

print "opening $ARGV[0]\n";
open ( F, "$ARGV[0]") or die $!;

print "reading $ARGV[0]\n";


my $stop = "#----------------------------------------#";
my $start = "Solution";

my $i = 0;
my $j = 0;
my $lines_to_read = 15;
while( my $line = <F>){

	if( $line =~ m/$start/g ){
		print $start."\n";
		while($j < $lines_to_read && $line !~ m/$stop/){
			$line = <F>
		}
		$j = 0;
	}else{
		print $line;
	}
$i++;


}

print "closing $ARGV[0]\n";
close F or die $!;
