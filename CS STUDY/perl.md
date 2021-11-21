# PERL

## perl 변수

### perl 변수 입력 받기(ARGV)
**[ ARGV ]**
Perl은 자동적으로 @ARGV라는 배열을 제공하며, 해당 배열에는 명령행에서 전달된 모든 값들이 담겨 있습니다.
* use strict을 사용하더라도 해당 변수는 따로 선언하지 않아도 됩니다.

**@ARGV에서 명령행 인자들을 추출하는 방법**
@ARGV는 평범한 Perl 배열입니다. perl 스크립트 내에서 생성하는 배열과 유일한 차이는, @ARGV는 선언할 필요가 없고 스크립트 시작 시 Perl에 의해 생성된다는 점입니다.
* @ARGV는 평범한 배열이기 때문에 $ARVG[0]과 같이 인덱스를 이용해 하나씩 접근할 수 있습니다.

```perl
#!/usr/bin/perl

my ($first, $second) = @ARGV;

my $first = $ARGV[0];
my $second = $ARGV[1];
```

**스크립트의 이름은 $0에 담깁니다.**
실행되는 스크립트의 이름은 항상 $0 변수에 담깁니다.

### 변수 합치기
Perl에서는 여러 개의 문자열을 하나로 연결할 때 마침표(.) 연산자를 사용합니다.
**[ 예시 ]**
```perl
#!/usr/bin/perl

my $first = $ARGV[0];
my $second = $ARGV[1];

my $result = "$first$second";
my $result2 = $first.$second;
my $str_result = "$first/$second"."TEST";

print $result;
print "\n";
print $result2;
print "\n";
print $str_result;
print "\n";
```
**[ 결과물 ]**
```bash
perl test.pl name number
namenumber
namenumber
name/numberTEST
```