# 웹 구성요소

- HTML : 구조

- CSS : 표현

- Javascript : 동작
  
  # 웹 표준

- 웹에서 표준적으로 사용되는 기술, 규칙

- 어떤 브라우저든 웹페이지가 동일하게 보이도록 함 (크로스브라우징)
  
  # 개발 환경 설정

- vscode 확장프로그램

- chrome 개발자 도구

# HTML

- Hyper Text Markup Language : 웹 페이지 작성 언어

- Hyper Text : 참조(하이퍼링크)를 통해 사용자가 한 문서에서 다른 문서로 즉시 접근할 수 있는 텍스트

- Markup Language : 태그 등을 통해 문서나 데이터의 구조를 명시하는 언어
  
  ## HTML 기본 구조

- html : 문서의 최상위(root) 요소

- head : 문서 메타데이터 요소
  
  - 문서 제목, 인코딩, 스타일, 외부 파일 로딩 등
  - 일반적으로 브라우저에 나타나지 않는 내용

- body : 문서 본문 요소
  
  - 실제 화면 구성과 관련된 내용

```html
<!DOCTYPEhtml>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
</head>
<body>

</body>
</html>
```

```html
<!DOCTYPEhtml>
head 예시
<title> : 브라우저 상단 타이틀
<meta> : 문서 레벨 메타데이터 요소
<link> : 외부 리소스 연결 요소
<script> : 스크립트 요소
<style> : CSS 직접 작성

<head>
    <title>HTML 수업</title>
    <meta charset = 'UTF-8'>
    <link href = 'style.css' rel = 'stylesheet'>
    <script src = 'javascript.js'></script>
    <style>
    p {
        color : blakc;
    }
```

#### Open Graph Protocol

- 메타 데이터를 표현하는 새로운 규약
  - HTML 문서의 메타 데이터를 통해 문서의 정보 전달
  - 메타정보에 해당하는 제목, 설명 등을 쓸 수 있도록 정의

## 요소(element)

```html
<!DOCTYPEhtml>
<h1>contents</h1>
HTML의 요소는 태그와 내용으로 구성되어있따
```

- HTML의 요소는 시작 태그와 종료 태그 그리고 태그 사이의 내용으로 구성
  
  - 요소는 태그로 내용의 성격과 의미를 정의
  - 내용이 없는 태그들도 존재 (br, hr, img, input, link, meta)

- 요소는 중첩 될 수 있음
  
  - 요소의 중첩으로 하나의 문서를 구조화
  
  - 여는 태그, 닫는 태그의 쌍을 잘 확인해야함
    
    - 오류를 반환하지않고 레이아웃이 깨진 상태로 출력되기 때문에 디버깅이 어려워짐
      
      ```html
      <!DOCTYPEhtml>
      <a href="https://google.com"></a>
      태그별로 사용할 수 있는 속성은 다르다
      공백 NO, "" 사용
      ```
      
      ## 속성(attribute)

- 속성을 통해 태그의 부가적 정보 설정 가능

- 요소는 속성을 가질 수 있으며 경로, 크기 등 추가적 정보 제공

- 요소의 시작 태그에 작성하며 이름과 값이 하나의 쌍으로 존재

- 태그와 상관없이 사용 가능한 속성(HTML Global Attribute) 존재
  
  - HTML Global Attribute
    
    - 모든 HTML 요소가 공통으로 사용할 수 있는 대표적인 속성
      
      - id : 문서 전체에서 유일한 고유 식별자 지정
      
      - class : 공백으로 구분된 해당 요소의 클래스 목록(CSS, JS에서 요소를 선택하거나 접근)
      
      - data-* : 페이지에 개인 사용자의 정의 데이터 저장
      
      - style : inline 스타일
      
      - title : 요소에 대한 추가 정보 지정
      
      - tabindex : 요소 탭 순서
        
        ```html
        <!DOCTYPE html>
        <html lang="en">
        <head>
        <meta charset="UTF-8">
        <title>Document</title>
        </head>
        <body>
        <!-- 이것은 주석입니다. -->
        <h1>나의 첫번째 HTML</h1>
        <p>이것은 본문입니다.</p>
        <span>이것은 인라인요소</span>
        <a href="https://www.naver.com">네이버로 이동!!</a>
        </body>
        </html>
        ```
        
        #### 렌더링

- 웹사이트 코드를 사용자가 보게 되는 웹사이트로 바꾸는 과정
  
  #### DOM트리

- 텍스트 파일인 HTML 문서를 브라우저에서 렌더링 하기 위한 구조
  
  - HTML 문서에 대한 모델을 구성
  
  - HTML 문서 내의 각 요소에 접근 / 수정에 필요한 프로퍼티와 메서드 제공
    
    ### 인라인 / 블록 요소

- HTML 요소는 크게 인라인 / 블록 요소로 나눔

- 인라인 요소는 글자처럼 췩브

- 블록 요소는 한 줄을 모두 사용
  
  ```html
  <a></a> : href 속성을 활용, 다른 URL로 연결하는 하이퍼링크 생성
  <b></b> : 굵은 글씨 요소
  <strong></strong> : 중요한 강조 요소
  <i></i> : 기울임 글씨 요소
  <em></em> : 중요한 강조 요소
  <br> : 텍스트 내 줄 바꿈 생성
  <img> : src 속성 활용 이미지 표현, alt 속성 활용 대체 텍스트
  <span></span> 의미없는 인라인 컨테이너
  <p></p> : 하나의 문단
  <hr> : 문단 레벨 요소에서의 주제의 분리를 의미하며 수평선으로 표현
  <ol></ol> : 순서가 있는 리스트
  <ul></ul> : 순서가 없는 리스트
  <pre></pre> : HTML에 작성한 내용을 그대로 표현, 보통 고정폭 글꼴, 공백 문자 유지
  <blockquote></blockquote> : 텍스트가 긴 인용문, 주로 들여쓰기를 한 것을 표현
  <div></div> : 의미없는 블록 레벨 컨테이너
  ```
  
  # CSS

- CSS : 스타일을 지정하기 위한 언어

- 스타일을 선택, 지정
  
  ```html
  <!DOCTYPEhtml>
  h1 {
    color: blue;
    font-size: 15px;
  }
  ```

- CSS 구문은 선택자를 통해 스타일을 지정할 HTML 요소를 선택

- 중괄호 안에서는 속성과 값, 하나의 쌍으로 이루어진 선언 진행

- 각 쌍은 선택한 요소의 속성, 속성에 부여 할 값 의미
  
  - 속성(Property) : 어떤 스타일 기능을 변경할지 결정
  
  - 값(Value) : 어떻게 스타일 기능을 변경할지 결정
    
    ### CSS 정의 방법

- 인라인(Inline)

- 내부참조(embedding) : `<style>`

- 외부 참조(link file) : 분리된 CSS 파일

```html
<!DOCTYPE html>
<!-- CSS 정의 방법 1 (인라인, 해당 태그에 직접 style 속성을 활용) -->
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1 style="color: blue; font-size: 100px;">Hello</h1>
</body>
</html>
```

```html
<!-- CSS 정의 방법 2 내부 참조, <head>태그 내에 <style>에 지정 -->
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        h1 {
            color: blue;
            font-size: 100px;
        }
    </style>
</head>
<body>
</body>
</html>
```

```html
<!-- CSS 정의 방법 3 (외부 참조, 외부 CSS 파일을 <head>내<link>를 통해 불러오기) -->
<html lang="en">
<head>
    <title>mySite</title>
    <link rel="stylesheet" href="mystyle.css">
</head>
<body>
    <h1>This is my site</h1>
</body>
</html>
```

```css
mystyle.css

h1 {
    color: blue;
    font-size: 20px
}
```

### CSS with 개발자 도구

- styles : 해당 요소에 선언된 모든 CSS

- computed : 해당 요소에 최종 계산된 CSS
  
  ### CSS 기초 선택자

- 요소 선택자
  
  - HTML 태그를 직접 선택

- 클래스(class) 선택자
  
  - 마침표(.)문자로 시작하며, 해당 클래스가 적용된 항목 선택

- 아이디(id) 선택자
  
  - '#' 문자로 시작하며 해당 아이디가 적용된 항목을 선택
  - 일반적으로 하나의 문서에 1번만 사용
  - 여러 번 사용해도 동작하지만, 단일 id 를 사용하는것을 권장