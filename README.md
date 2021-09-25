## TRIPPERS

[시연 영상 보기](https://tv.kakao.com/v/419944191)

## 🚩 목차


1. [프로젝트 개요](#-프로젝트-개요)
2. [사용 패키지](#-package)
3. [기능 소개](#-기능-소개)


## 🎬 프로젝트 개요


여행을 좋아하는 사람들의 여행 후기 플랫폼!
- 직접 다녀온 여행지의 사진과 후기를 기록하고 다른 유저들과 공유할 수 있습니다


## 🗓 프로젝트 기간


2021년 6월 7일 ~ 2021년 6월 10일


## 💁🏻‍♂️ 팀원 소개


황준연(팀장), 이선택, 곽아름, 이윤주


## 📝 와이어프레임

### 1. 로그인페이지 
<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FqjfS7%2FbtrdevO2Qu7%2FjFwiGp6hupvKNVvPyodjj1%2Fimg.png" width="500">

### 2. 회원가입페이지
<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FcmNNBx%2Fbtrdj59m7ID%2FokLgjCRKj4y6wHpKTX1NE1%2Fimg.png" width="500"> 

### 3. 메인페이지
<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fb8jxw3%2Fbtq6EVz2KTY%2FBkjrtmUJPhO69K3J4bxsRK%2Fimg.png" width="500"> 

### 4. 상세페이지
<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FcvIBly%2FbtrdopTsnC2%2Fm0NM3z7kyQx4gYBt8HKcTK%2Fimg.png" width="500"> 

### 5. 여행리뷰작성페이지
<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbJEgtF%2FbtrdmB0V1AM%2Fx3VaasB2HeKKzkH6ZisXMk%2Fimg.png" width="500"> 

### 6. 여행리뷰수정페이지
<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FcocaEy%2Fbtq6LVrTEoL%2FVEhKN3xowlWj3YqGEk8ZP0%2Fimg.png" width="500"> 



## 🛠 Package


HTML, CSS(Bulma, Bootstrap, Font Awesome), Javascript(Ajax), Python(pymongo, flask), AWS EC2


## 💡 기능 소개


- JWT토큰 인증 방식을 적용한 로그인 구현
- 로그인 및 회원가입 페이지에서 중복체크를 포함한 유효성 검사
- Jinja2 템플릿 엔진을 이용한 서버사이드 렌더링
- 여행 리뷰 게시글 작성시 이미지 업로드 기능
- 여행 리뷰 게시글 작성, 수정, 삭제를 포함한 CRUD 기능 구현
- 메인페이지, 리뷰 상세페이지에서 ajax의 POST, GET 방식으로 각각 포스팅 API와 리스팅 API 구현
