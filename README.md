# NoslegumaDarbs2

## Manuālis visu nepieciešamo uzstādīšanai: Lai lietotne darbotos pareizi, nepieciešama pareiza Edge draivera versija.

Lai noskaidrotu, kāda versija nepieciešama, atveriet Edge pārlūkprogrammas iestatījumus (trīs punkti augšējā labajā stūrī) -> _“Palīdzība un atsauksmes”_ -> _“Par Microsoft Edge programmu”_.
Versija izskatīsies šādi: _“Versija 136.0.3240.64 (64 bitu versija)”_.

Lai lejupielādētu Edge draiveri, dodieties uz oficiālo saiti (https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/?form=MA13LH) un zemāk izvēlieties jūsu pārlūka versiju.
Atarhivējiet draiveri un ievietojiet tikai .exe failu mapē EdgeDriver projektā GitHub.
(Lai būtu ērtāk, noklonējiet projektu uz savu datoru ar komandu git clone saite uz projektu un atveriet to VS Code programmā.)

Nepieciešams uzstādīts Python ar *versiju 3.11.9 (stabilākā versija)*. Lejupielādējiet to no oficiālās mājaslapas (https://www.python.org/downloads/windows/).
Instalācijā atzīmējiet -> _Add Python to PATH_ -> _Install now_

Uzrakstiet terminalā 2 komandas(pēc Python instalēšanas): 
1)pip install chromedriver-autoinstaller
2)pip install selenium

 
Lai komanda 1 noteikti darbotos, šajās vietās jāievada lietotājvārds (By.ID, "IDToken1").send_keys("") un parole (By.ID, "IDToken2").send_keys("")

## projekta paraksts

Projekts ir programma, kas ļauj ātri atvērt tīmekļa lapas pārlūkprogrammā un automātiski logot lietotāju, kā arī nodrošina iespēju nosūtīt tekstu tulkošanai un automātiski atvērt tulkotāja lapu.
Tas ļauj automatizēt rutīnas pieslēgšanos Ortus vietnei un novērš nepieciešamību katru reizi atsevišķi atvērt tulkotāju.

## Lietošanas instrukcija

1) Lai palaistu programmu, ievadiet terminālī python main.py
2) Izvēlieties skaitli no 1 līdz 4, lai izvēlētos vajadzīgo vietni
3) Lai izietu no programmas, ievadiet 0
4) Izvēloties tulkotāju (4. komanda), ievadiet tekstu, kuru vēlaties iztulkot, un nospiediet ENTER

## Piezīmes: 
Konsolē var parādīties kļūdas:

DevTools listening on ws://127.0.0.1:60069/devtools/browser/7d64a4ab-cc41-48d2-b0cf-f2a282040a8b 
[50996:23988:0512/211524.190:ERROR:components\edge_auth\edge_auth_errors.cc:531] EDGE_IDENTITY: Get Default OS Account failed:  
Error: Primary Error: kTokenRequestFailed, Secondary Error: kTokenFetchUserInteractionRequired,  
Platform error: -2147186499, hex:800488bd, Error string: Error code: 0x800488bd, error message:Error

Šīs kļūdas norāda, ka pārlūks mēģina piekļūt lietotāja kontam. Tas ir normāli, un kods netiek pārtraukts šo kļūdu dēļ.