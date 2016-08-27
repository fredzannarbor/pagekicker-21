#!/usr/local/bin/perl -w
use strict;

# (1) quit unless we have the correct number of command-line args
$num_args = $#ARGV + 1;
if ($num_args != 1) {
    print "\nUsage: quoted sentence for Yoda to speak.\n";
    exit;
}


my @sentences = ('I will teach you',
                 'The truth is out there',
                 'That is an Imperial shuttle',
                 'My husband is giant dork',      #this is my wife's suggestion
                 'These fish are tasty'
                );

foreach (@sentences) {
    print yoda($_)."\n";
}

sub yoda {
    my ($sentence) = @_;

    my @pivot_words = qw/is be will show do try are teach have/;
    
    # Find out if I have a pivot word and grab the one with the lowest index
    my $pivot = (sort { $a->[1] <=> $b->[1]}
                 grep {$_->[1] > 0} 
                 map  { [" $_ ",index($sentence," $_ ")] } @pivot_words)[0];
                        #^^^^^^                 ^^^^^^^
                                                # Change to fix the problem [zdog]
                                                # pointed out - THX [zdog]

    # No pivot words
    return $sentence if (!$pivot);

    # Pivot the sentence
    $sentence = substr($sentence,$pivot->[1]+length($pivot->[0]),length($sentence)).
                " ".
                substr($sentence,0,$pivot->[1]).
                $pivot->[0];
    
    # Clear leading spaces
    $sentence =~ s/^\s+//;

    # Sentence case
    $sentence = ucfirst(lc($sentence));
}
