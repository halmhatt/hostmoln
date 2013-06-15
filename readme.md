# Höstmoln
Kod på Svenska som görs om till webbsida (HTML)

## Vad är Höstmoln?
Höstmoln är ett [programmeringsspråk](http://sv.wikipedia.org/wiki/Programspr%C3%A5k) som är skrivet på **Svenska**. 
Det är *enkelt att lära sig och enkelt att läsa*.
Koden görs sedan om till *HTML* som är det språk som används för att göra webbsidor, **koden görs alltså om till en webbsida!**


## Installera
För att installera *Höstmoln* så behövs något som heter *Python*, väldigt krångligt tyvärr. 

Jag ska försöka få till det enklare så att det bara går att trycka **installera**.

## Börja koda
Nu är det dags att börja koda. För att koda behöver man ett program där man kan skriva text. *Word* kanske du tänker, men det är lite för stort. Word skapar filer som innehåller *färger, storlek på text, bilder...*, vi vill ha ett program som **bara skriver text**. 

### Skapa din första sida
Det enklaste sättet att hitta ett sådant program är att öppna filen `min-första-sida.txt` i mappen `sidor`. 
Den ser ut såhär:

	RUBRIK
		Min första sida!
		
### Fyll på din sida
Perfekt! Det här är din första sida (och den är redan klar). Nu kan du fylla på sin sida genom att skriva mer saker.

Du kan tex lägga till en bild genom att skriva detta under:

	BILD 'min-katt.jpg'
	
Hela koden ser nu ut såhär:
	
	RUBRIK
		Min första sida!
	BILD 'min-katt.jpg'
	
## Hur funkar det
Hur funkar då det här språket? Jo det fungerar såhär:

### Indrag
Höstmoln bygger på att texten **"ser snygg ut"**. Lade du märke till att texten *"Min första sida!"* stod en bit in från kanten?
Detta kallas **indrag** och är väldigt viktigt. Det betyder att texten *"Min första sida"* **ligger i RUBRIK**. 
Om vi hade skrivit såhär istället:

	RUBRIK
	Min första sida!
	BILD 'min-katt.jpg'
	
så hade vi först fått en RUBRIK som var tom. Sedan texten *Min första sida!* **under rubriken** och sedan en bild på en katt.

Så för att **lägga någonting i någonting annat** så måste det vara inskjutet **1 tab** eller **4 mellanslag**. 
**Tab** heter den tangenten som ligger *till vänster om Q*, tryck på den *1 gång* eller *mellanslag 4 gånger*

### Ny rad
Vissa saker behöver även stå på en ny rad. Du gör en ny rad genom att trycka på **enter**, den största knappen på tangentbordet.

Du fick nyss lära dig om **indrag**, men texten *"Min första sida!"* stod även på en egen rad, under *RUBRIK*. Det är för att varje ny **grej** måste stå på en egen rad. En grej är tex: **RUBRIK, BILD, LÄNK**.

Det skulle alltså inte gå att skriva såhär:

	RUBRIK Min första sida! BILD 'min-katt.jpg'
	
då skulle det inte bli någonting. Dessutom blir det lättare att läsa om det skrivs på olika rader och med indrag.

### Grejer
Grejer kanske inte är något bra ord, men det går att göra olika *grejer* såsom *bilder, rubriker, länkar, listor...*. 

Varje grejs namn måste stå med **STORA BOKSTÄVER**. Här är en lista med alla grejer som finns nu:

* RUBRIK
* BILD
* LÄNK
* TEXT eller STYCKE
* LISTA
* NUMMER
* CITAT
* RUTA
* KOD
* HTML

Och alla dessa skrivs såhär:

	GREJ
		Saker som hamnar i grej (BILD kan inte ha saker i sig)
		
En förklaring på varje kommer längre ner.

Det finns även grejer som kan stå **i text** och inte kan ha saker i sig, dessa är:

* NY RAD

Ny rad används såhär:

	TEXT
		Det här är mitt tips: NY RAD
		Använd inte schampo till kroppen!
		
Då kommer det bli en ny rad där. Men man kan ju undra varför det inte blir ny rad automatiskt. Ibland kan raderna bli så långa att man inte kan se slutet när man skriver, då kan man dela upp det på två rader, såhär:

	TEXT
		Den här meningen kommer bli väldigt lång, och 
		då kanske jag inte ser slutet när jag sitter och
		skriver, så istället delar jag upp det på flera rader. 
		Men detta märks inte sen.
		
### RUBRIK
En rubrik visas med stor text, precis som man kanske kan tro. Man gör en rubrik såhär:

	RUBRIK
		Min rubriktext

### BILD
En bild visar en bild som du har lagt i mappen `bilder`. Du skriver vilken bild genom att skriva namnet på bilden.
Såhär lägger du till en bild:

	BILD 'min-katt.jpg'
	
Den där bilden skulle alltså vara den som ligger i mappen `bilder` och heter `min-katt.jpg`. 
Hela adressen blir då `bilder/min-katt.jpg`. `.jpg` i slutet av namnet skall vara samma som filen heter, 
det brukar vara `.jpg` men kan också vara tex `.jpeg`, `.gif` eller `.png`.

### LÄNK
En länk är något man kan **klicka på**. En länk har alltid en **adress**, och dit kommer man om man klickar på den.
Du skapar en länk genom att skriva såhär:

	LÄNK till SIDA 'mina-hundar'
		Klicka här för att se mina hundar
		
Den här länken går till din sida `mina-hundar` i mappen `sidor` (om du har en sådan)

Om du vill länka till en annan sida, som tex *Google* gör du såhär:

	LÄNK till 'www.google.com'
		Klicka här för att komma till Google
		
*Om addressen du länkar till inte börjar med `www.` måste du skriva `http://` innan, tyvärr. Då skriver du såhär:*

	LÄNK till 'http://google.com'
		Klicka här för att komma till Google (också)

Ibland kanske du vill länka till en *bild*, då skriver du såhär:

	LÄNK till BILD 'min-fina-katt.jpg'
		Titta min fina katt!
		
Om man klickar på den länken får man se bilden `min-fina-katt.jpg` som ligger i mappen `bilder`.

### TEXT och STYCKE
Text används för att skriva text. Det går att skriva text utan att först skriva TEXT ovanför, men om man skriver TEXT ovanför 
kan man ändra hur texten ser ut. Det finns mer information om detta längre ner i kapitlet **Stilar**.

För att skriva text gör du såhär:

	TEXT
		Min fina text
		
Du kan även strunta i TEXT:
	
	Min fina text
	
men då kan du inte ändra hur den ser ut. Detta kan du göra såhär:

	TEXT .blå
		Min fina Blåa text
		
	TEXT .grön
		Min fina Gröna text
		
Skillnaden mellan `TEXT` och `STYCKE` är att ett `STYCKE` är gjort för mycket text, och olika stycken har en tom rad mellan sig. 
`TEXT` däremot har inget mellanrum mellan olika texter. Här är ett exempel:

	TEXT .blå
		Hej
	TEXT .grön
		Jacob
		
Det här exemplet blir alltså såhär: *"Hej Jacob"* där *"Hej"* är blått och *"Jacob"* är grönt. Om vi hade gjort såhär:

	STYCKE .blå
		Hej
		
	STYCKE .grön
		Jacob
		
Färgerna blir likadana men först står det *"Hej"* på en egen rad, sedan en till innan *"Jacob"*, typ såhär:

	Hej
	
	Jacob
	
Inte riktigt det du tänkt kanske.
		
### LISTA och NUMMER
NUMMER är en LISTA fast med nummer framför. Det här är en LISTA:

* Hej
* Hej igen
* Hej igen igen

Du gör en lista såhär:
	
	LISTA
		- Hej
		- Hej igen
		- Hej igen igen
		
Man skriver alltså först `LISTA` och sedan gör man en ny rad för varje grej, och sätter ett *sträck* (`-`) framför.

Och det här är NUMMER:
1. Hej
2. Hej igen
3. Hej igen igen

Du gör en numrerad lista såhär:

	NUMMER
		1. Hej
		2. Hej igen
		3. Hej igen igen
		
Man skriver alltså först `NUMMER` och sedan gör man en ny rad för varje grej, och sätter ett *nummer och en punkt* (`1.`) framför.
Man behöver inte vara så duktig med numren, alla nummer går bra, men det blir alltid 1, 2, 3, 4, 5. Det här funkar tex:

	NUMMER
		1. Hej
		32. Hej igen
		12. Hej igen igen
		
Men det blir ändå såhär:

1. Hej
2. Hej igen
3. Hej igen igen

### CITAT
Ett citat kan vara något kul som någon har sagt eller ett mer klassiskt citat som du har sett. Du gör ett såhär:

	CITAT
		Den finaste fisken är inte den vackraste, kanske...
		
Och detta går då att få till som ett **riktigt snyggt citat**.

### RUTA
En `RUTA` används för att lägga saker i varandra, men också för att man ibland vill ha en snygg ruta runt något. 
En `RUTA` är helt genomskinlig om du inte lägger till någon *klass*. Det här blir en genomskinlig ruta:

	RUTA
		TEXT
			Hej mannen
			
Medan den här blir blå:

	RUTA .blå
		TEXT
			Hej mannen
			
Ibland behövs inte rutan, exemplet ovan skulle kunna gjorts såhär:

	STYCKE .blå
		Hej mannen
		
### KOD
Ibland vill du visa någon hur du har gjort, alltså den kod du har skrivit. Detta gör du med `KOD`, här är ett exempel:

	KOD
		RUTA .blå
			TEXT
				Hej mannen
				
Det här kommer **inte** bli en `RUTA` med `TEXT` *"Hej mannen"* utan bara en `KOD` där du ser koden. 
Det är så alla de här exemplen är gjorda.

Det går även att använd all annan typ av kod, text `html`:

	KOD
		<footer>
			Min footer
		</footer>

### HTML
När du börjar växa ur **Höstmoln** eller vill testa lite *HTML* så kan du göra det **i Höstmoln** istället för att byta 
helt till *HTML*. Detta gör du genom att använda `HTML`. Allting du skriver i en `HTML` ruta kommer stå kvar som det står, 
du kan **inte använda Höstmoln inuti** en `HTML` ruta.

Här är ett exempel på en rubrik 2:
	
	HTML
		<h2>Hej hej</h2>
		
Detta blir då en *Rubrik 2* något som finns i HTML, en lite mindre rubrik.

**Det här fungerar inte**:

	HTML
		<div>
			RUTA
				Hej
		</div>

*Det går inte använda Höstmoln i HTML rutor*

## Gör om koden till en webbsida
När du vill göra om din `Höstmoln`:kod till en webbsida använder du programmet `compile.py`:

	python3 compile.py sidor/dinsida.txt
	
Du använder `python3` och filen `compile.py` för att göra om din fil `sidor/dinsida.txt`, 
här är `dinsida.txt` den sida du har gjort.

Ett tips är att spara dina sidor som `.moln` för att enkelt se att det är **Höstmoln**-filer.
Då gör du om dem såhär:
	
	python3 comile.py sidor/dinsida.moln
	
### Spara filen
För att spara filen gör du såhär:

	python3 compile.py sidor/dinsida.moln sidor/dinsida.html

eller såhär:
	
	python3 compile.py sidor/dinsida.moln > sidor/dinsida.html

## Använd din webbsida
När du har filen `dinsida.html` så kan du bara dubbelklicka på den för att öppna. Då ser du din sida i din **webbläsare**.

För att någon ska kunna se din webbsida hemifrån sig så krävs tyvärr lite jobb, men förhoppningsvis kommer detta bli enklare.
Då behöver du ett **webbhotell**, sök på det på [Google](http://google.com) så finns det flera.

## Vad är ett programmeringsspråk?
Ett programmeringsspråk är ett sätt att *prata med datorn*. Du skriver *till datorn* och datorn kan då göra vissa saker. 
Det vi gör med **Höstmoln** är att tala om för datorn **hur vi vill att vår webbsida ska se ut**. 

Datorn förstår bara *HTML* och inte **Höstmoln** när man ska göra webbsidor, därför måste man göra om **Höstmoln** till *HTML*.
Man kan säga att vi *tolkar* till datorn.

Så när du kodar **Höstmoln** så förstår tillslut datorn vad du menar, vad skönt va?

