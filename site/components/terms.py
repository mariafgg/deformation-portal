from dash import html, dcc
import dash_bootstrap_components as dbc

# Updated text component with white background, blue titles/subtitles, and black text
text = html.Div([
    dbc.Container([
        html.H3("Notkunarskilmálar", className="mt-5", style={'color': '#004c80', 'fontWeight': 'bold'}),
        html.H5("Leiðbeiningar varðandi endurnot upplýsinga í GNSS vefsjá Veðurstofu íslands, GNSS-gáttin.", style={'color': '#004c80', 'fontWeight': 'bold'}),
        html.P("sbr. 5. gr. laga nr. 45/2018 um endurnot opinberra upplýsinga. Veðurstofa Íslands hvetur alla til að nota og endurnýta þær upplýsingar sem eru gerðar aðgengilegar með GNSS-gáttinni að uppfylltum eftirfarandi skilyrðum.", style={'color': 'black'}),
        html.H5("Notkun upplýsinga", style={'color': '#004c80', 'fontWeight': 'bold'}),
        html.P("Með notkun gagna sem eru gerð aðgengileg með GNSS-gáttinni (hér eftir kallað „upplýsingarnar“) telst þú hafa samþykkt eftirfarandi skilmála og skilyrði.", style={'color': 'black'}),
        html.P("Veðurstofa Íslands veitir þér ótímabundna heimild til varanlegrar notkunar upplýsinganna hvar sem er, án gjaldtöku og gefur eftir einkarétt sinn, sé honum til að dreifa, að uppfylltum skilyrðunum hér fyrir neðan.", style={'color': 'black'}),
        html.H5("Notandi má:", style={'color': '#004c80', 'fontWeight': 'bold'}),
        html.Ul([
            html.Li("afrita, birta, dreifa og senda upplýsingarnar,", style={'color': 'black'}),
            html.Li("aðlaga upplýsingarnar,", style={'color': 'black'}),
            html.Li("endurnýta upplýsingarnar, þar með talið í hagnaðarskyni til dæmis með því að setja þær saman við aðrar upplýsingar eða með því að hafa upplýsingarnar sem hluta af vöru eða hugbúnaði.", style={'color': 'black'}),
        ], style={'color': 'black'}),
        html.H5("Notandi verður að:", style={'color': '#004c80', 'fontWeight': 'bold'}),
        html.Ul([
            html.Li("Taka fram að þær upplýsingar sem byggt er á eigi uppruna í GNSS kerfi Veðurstofu Íslands með eftirfarandi texta: „Byggt á gögnum frá Veðurstofu Íslands.“ Einnig skal vísa í þessa skilmála þar sem því verður við komið.", style={'color': 'black'}),
            html.Li("Gæta þess að skýrt komi fram hver ber ábyrgð á vinnslu upplýsinganna þegar þær eru gerðar öðrum aðgengilegar.", style={'color': 'black'}),
            html.Li("Gæta þess að endurnot upplýsinganna brjóti ekki í bága við lög þ.m.t. ákvæði almennra hegningarlaga, laga um vernd hugverkaréttinda og laga um persónuvernd og vinnslu persónuupplýsinga, eða önnur réttindi þriðja manns.", style={'color': 'black'}),
        ], style={'color': 'black'}),
        html.H5("Ekkert samþykki", style={'color': '#004c80', 'fontWeight': 'bold'}),
        html.P("Notkun upplýsinganna gefur notanda hvorki heimild til að gefa til kynna að hann sé í opinberri stöðu né að Veðurstofa Íslands hafi samþykkt notkun hans á upplýsingunum sérstaklega.", style={'color': 'black'}),
        html.H5("Engin ábyrgð", style={'color': '#004c80', 'fontWeight': 'bold'}),
        html.P("Veðurstofa Íslands er undanskilin fyrirsvari, ábyrgð, skyldum og skaðabótum í tengslum við upplýsingar fengnar með GNSS-gáttinni að því marki sem lög leyfa.", style={'color': 'black'}),
        html.P("Veðurstofa Íslands ber ekki ábyrgð á villum eða vanskráningu upplýsinga í GNSS-gáttinni eða gagna úr GNSS kerfi stofnunarinnar sem GNSS-gáttin byggir á og er ekki ábyrg fyrir neinu tapi, meiðslum eða skaða sem hlýst af notkun þeirra.", style={'color': 'black'}),
        html.H5("Fyrirvarar", style={'color': '#004c80', 'fontWeight': 'bold'}),
        html.P("Upplýsingar sem notandi fær með GNSS-gáttinni eru afhentar eins og þær eru og í þeim kunna að vera villur og ónákvæmni um tímasetningu, staðsetningu og færslur.", style={'color': 'black'}),
        html.P("GNSS-gáttin virkar með vel flestum nýrri útgáfum af vöfrum en á því kunna að vera undantekningar sem Veðurstofa Íslands verður ekki gerð ábyrg fyrir.", style={'color': 'black'}),
        html.H5("Aðgengi og persónuupplýsingar", style={'color': '#004c80', 'fontWeight': 'bold'}),
        html.P("GNSS-gáttin er aðgengileg án skráningar á opnu vefsvæði og Veðurstofa Íslands skráir ekki upplýsingar um notendur GNSS-gáttarinnar.", style={'color': 'black'}),
        html.H5("Tilvísanir", style={'color': '#004c80', 'fontWeight': 'bold'}),
        html.P("Þessar leiðbeiningar byggja á lögum nr. 42/2018 um endurnot opinberra upplýsinga. Einnig voru höfð til hliðsjónar breska „Open government licence“ http://www.nationalarchives.gov.uk/doc/open-government-licence/version/3", style={'color': 'black'}),
    ], style={'backgroundColor': 'white', 'padding': '20px'})
], style={'backgroundColor': 'white'})

