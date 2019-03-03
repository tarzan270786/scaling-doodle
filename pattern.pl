#!/usr/bin/perl
my $var="Hello this is perl prgoramming";
if($var=~m/perl/)
{
		print "true\n";
	        print "$'\n"; # this contains after the pattern is matched 
                print "$&\n" ; # this prints the pattern 
		print "$`\n"; # this contains before the pattern is matched 	
	} 
	else
	{
			print "False\n"; 
		}

my $a="Hello how are you";
$a=~s/hello/cello/gi;
print "$a\n";


