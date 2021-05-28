## net.ipv4.tcp_tw_recycle 
TW State의 개수를 줄여주어 Session Resource를 많이 확보해주기때문에 추천되는 Parameter 입니다.  

## net.ipv4.tcp_tw_reuse 
빠른 장애 복구를 위해(즉시 기존 Session 재사용) 추천되는 Parameter 입니다. 

```bash
@netstat -napo | grep -i time_wait | wc -l@
```

위 명령어 사용 시 time_wait 걸린 경우가 많아서 위 설정 넣은 것(최대 8000개 정도까지 있었음) 

 