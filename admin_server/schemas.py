from typing import Annotated, Literal

from pydantic import (BaseModel, UUID4, EmailStr, Field, ConfigDict, AfterValidator, UrlConstraints, AnyUrl,
                      NaiveDatetime)

from .utils.validators import try_to_construct_jwk


class UserRegister(BaseModel):
    login: EmailStr
    passwd: str


class UserIn(BaseModel):
    name: str | None = None
    surname: str | None = None
    patronymic: str | None = None


class UserOut(UserIn):
    id: UUID4


HttpsUrl = Annotated[AnyUrl, UrlConstraints(max_length=2083, allowed_schemes=["https"])]
GrantTypes = Literal[
    "authorization_code", "implicit", "password", "client_credentials", "refresh_token",
    "urn:ietf:params:oauth:grant-type:jwt-bearer", "urn:ietf:params:oauth:grant-type:saml2-bearer"
]
ResponseTypes = Literal["code", "token"]

JWK = Annotated[dict, AfterValidator(try_to_construct_jwk)]


class ClientNameLangs(BaseModel):
    client_name_af_za: str | None = Field(alias="client_name#af-ZA", title="Client name (Afrikaans (South Africa))",
                                          default=None, placeholder="Client name (Afrikaans (South Africa))")
    client_name_ar_ae: str | None = Field(alias="client_name#ar-AE", title="Client name (Arabic (U.A.E.))",
                                          default=None, placeholder="Client name (Arabic (U.A.E.))")
    client_name_ar_bh: str | None = Field(alias="client_name#ar-BH", title="Client name (Arabic (Bahrain))",
                                          default=None, placeholder="Client name (Arabic (Bahrain))")
    client_name_ar_dz: str | None = Field(alias="client_name#ar-DZ", title="Client name (Arabic (Algeria))",
                                          default=None, placeholder="Client name (Arabic (Algeria))")
    client_name_ar_eg: str | None = Field(alias="client_name#ar-EG", title="Client name (Arabic (Egypt))", default=None,
                                          placeholder="Client name (Arabic (Egypt))")
    client_name_ar_iq: str | None = Field(alias="client_name#ar-IQ", title="Client name (Arabic (Iraq))", default=None,
                                          placeholder="Client name (Arabic (Iraq))")
    client_name_ar_jo: str | None = Field(alias="client_name#ar-JO", title="Client name (Arabic (Jordan))",
                                          default=None, placeholder="Client name (Arabic (Jordan))")
    client_name_ar_kw: str | None = Field(alias="client_name#ar-KW", title="Client name (Arabic (Kuwait))",
                                          default=None, placeholder="Client name (Arabic (Kuwait))")
    client_name_ar_lb: str | None = Field(alias="client_name#ar-LB", title="Client name (Arabic (Lebanon))",
                                          default=None, placeholder="Client name (Arabic (Lebanon))")
    client_name_ar_ly: str | None = Field(alias="client_name#ar-LY", title="Client name (Arabic (Libya))", default=None,
                                          placeholder="Client name (Arabic (Libya))")
    client_name_ar_ma: str | None = Field(alias="client_name#ar-MA", title="Client name (Arabic (Morocco))",
                                          default=None, placeholder="Client name (Arabic (Morocco))")
    client_name_ar_om: str | None = Field(alias="client_name#ar-OM", title="Client name (Arabic (Oman))", default=None,
                                          placeholder="Client name (Arabic (Oman))")
    client_name_ar_qa: str | None = Field(alias="client_name#ar-QA", title="Client name (Arabic (Qatar))", default=None,
                                          placeholder="Client name (Arabic (Qatar))")
    client_name_ar_sa: str | None = Field(alias="client_name#ar-SA", title="Client name (Arabic (Saudi Arabia))",
                                          default=None, placeholder="Client name (Arabic (Saudi Arabia))")
    client_name_ar_sy: str | None = Field(alias="client_name#ar-SY", title="Client name (Arabic (Syria))", default=None,
                                          placeholder="Client name (Arabic (Syria))")
    client_name_ar_tn: str | None = Field(alias="client_name#ar-TN", title="Client name (Arabic (Tunisia))",
                                          default=None, placeholder="Client name (Arabic (Tunisia))")
    client_name_ar_ye: str | None = Field(alias="client_name#ar-YE", title="Client name (Arabic (Yemen))", default=None,
                                          placeholder="Client name (Arabic (Yemen))")
    client_name_az_az: str | None = Field(alias="client_name#az-AZ", title="Client name (Azeri (Latin) (Azerbaijan))",
                                          default=None, placeholder="Client name (Azeri (Latin) (Azerbaijan))")
    client_name_az_cyrl_az: str | None = Field(alias="client_name#az-Cyrl-AZ",
                                               title="Client name (Azeri (Cyrillic) (Azerbaijan))", default=None,
                                               placeholder="Client name (Azeri (Cyrillic) (Azerbaijan))")
    client_name_be_by: str | None = Field(alias="client_name#be-BY", title="Client name (Belarusian (Belarus))",
                                          default=None, placeholder="Client name (Belarusian (Belarus))")
    client_name_bg_bg: str | None = Field(alias="client_name#bg-BG", title="Client name (Bulgarian (Bulgaria))",
                                          default=None, placeholder="Client name (Bulgarian (Bulgaria))")
    client_name_bs_ba: str | None = Field(alias="client_name#bs-BA",
                                          title="Client name (Bosnian (Bosnia and Herzegovina))", default=None,
                                          placeholder="Client name (Bosnian (Bosnia and Herzegovina))")
    client_name_ca_es: str | None = Field(alias="client_name#ca-ES", title="Client name (Catalan (Spain))",
                                          default=None, placeholder="Client name (Catalan (Spain))")
    client_name_cs_cz: str | None = Field(alias="client_name#cs-CZ", title="Client name (Czech (Czech Republic))",
                                          default=None, placeholder="Client name (Czech (Czech Republic))")
    client_name_cy_gb: str | None = Field(alias="client_name#cy-GB", title="Client name (Welsh (United Kingdom))",
                                          default=None, placeholder="Client name (Welsh (United Kingdom))")
    client_name_da_dk: str | None = Field(alias="client_name#da-DK", title="Client name (Danish (Denmark))",
                                          default=None, placeholder="Client name (Danish (Denmark))")
    client_name_de_at: str | None = Field(alias="client_name#de-AT", title="Client name (German (Austria))",
                                          default=None, placeholder="Client name (German (Austria))")
    client_name_de_ch: str | None = Field(alias="client_name#de-CH", title="Client name (German (Switzerland))",
                                          default=None, placeholder="Client name (German (Switzerland))")
    client_name_de_de: str | None = Field(alias="client_name#de-DE", title="Client name (German (Germany))",
                                          default=None, placeholder="Client name (German (Germany))")
    client_name_de_li: str | None = Field(alias="client_name#de-LI", title="Client name (German (Liechtenstein))",
                                          default=None, placeholder="Client name (German (Liechtenstein))")
    client_name_de_lu: str | None = Field(alias="client_name#de-LU", title="Client name (German (Luxembourg))",
                                          default=None, placeholder="Client name (German (Luxembourg))")
    client_name_dv_mv: str | None = Field(alias="client_name#dv-MV", title="Client name (Divehi (Maldives))",
                                          default=None, placeholder="Client name (Divehi (Maldives))")
    client_name_el_gr: str | None = Field(alias="client_name#el-GR", title="Client name (Greek (Greece))", default=None,
                                          placeholder="Client name (Greek (Greece))")
    client_name_en_au: str | None = Field(alias="client_name#en-AU", title="Client name (English (Australia))",
                                          default=None, placeholder="Client name (English (Australia))")
    client_name_en_bz: str | None = Field(alias="client_name#en-BZ", title="Client name (English (Belize))",
                                          default=None, placeholder="Client name (English (Belize))")
    client_name_en_ca: str | None = Field(alias="client_name#en-CA", title="Client name (English (Canada))",
                                          default=None, placeholder="Client name (English (Canada))")
    client_name_en_cb: str | None = Field(alias="client_name#en-CB", title="Client name (English (Caribbean))",
                                          default=None, placeholder="Client name (English (Caribbean))")
    client_name_en_gb: str | None = Field(alias="client_name#en-GB", title="Client name (English (United Kingdom))",
                                          default=None, placeholder="Client name (English (United Kingdom))")
    client_name_en_ie: str | None = Field(alias="client_name#en-IE", title="Client name (English (Ireland))",
                                          default=None, placeholder="Client name (English (Ireland))")
    client_name_en_jm: str | None = Field(alias="client_name#en-JM", title="Client name (English (Jamaica))",
                                          default=None, placeholder="Client name (English (Jamaica))")
    client_name_en_nz: str | None = Field(alias="client_name#en-NZ", title="Client name (English (New Zealand))",
                                          default=None, placeholder="Client name (English (New Zealand))")
    client_name_en_ph: str | None = Field(alias="client_name#en-PH",
                                          title="Client name (English (Republic of the Philippines))", default=None,
                                          placeholder="Client name (English (Republic of the Philippines))")
    client_name_en_tt: str | None = Field(alias="client_name#en-TT",
                                          title="Client name (English (Trinidad and Tobago))", default=None,
                                          placeholder="Client name (English (Trinidad and Tobago))")
    client_name_en_us: str | None = Field(alias="client_name#en-US", title="Client name (English (United States))",
                                          default=None, placeholder="Client name (English (United States))")
    client_name_en_za: str | None = Field(alias="client_name#en-ZA", title="Client name (English (South Africa))",
                                          default=None, placeholder="Client name (English (South Africa))")
    client_name_en_zw: str | None = Field(alias="client_name#en-ZW", title="Client name (English (Zimbabwe))",
                                          default=None, placeholder="Client name (English (Zimbabwe))")
    client_name_es_ar: str | None = Field(alias="client_name#es-AR", title="Client name (Spanish (Argentina))",
                                          default=None, placeholder="Client name (Spanish (Argentina))")
    client_name_es_bo: str | None = Field(alias="client_name#es-BO", title="Client name (Spanish (Bolivia))",
                                          default=None, placeholder="Client name (Spanish (Bolivia))")
    client_name_es_cl: str | None = Field(alias="client_name#es-CL", title="Client name (Spanish (Chile))",
                                          default=None, placeholder="Client name (Spanish (Chile))")
    client_name_es_co: str | None = Field(alias="client_name#es-CO", title="Client name (Spanish (Colombia))",
                                          default=None, placeholder="Client name (Spanish (Colombia))")
    client_name_es_cr: str | None = Field(alias="client_name#es-CR", title="Client name (Spanish (Costa Rica))",
                                          default=None, placeholder="Client name (Spanish (Costa Rica))")
    client_name_es_do: str | None = Field(alias="client_name#es-DO", title="Client name (Spanish (Dominican Republic))",
                                          default=None, placeholder="Client name (Spanish (Dominican Republic))")
    client_name_es_ec: str | None = Field(alias="client_name#es-EC", title="Client name (Spanish (Ecuador))",
                                          default=None, placeholder="Client name (Spanish (Ecuador))")
    client_name_es_es: str | None = Field(alias="client_name#es-ES", title="Client name (Spanish (Spain))",
                                          default=None, placeholder="Client name (Spanish (Spain))")
    client_name_es_gt: str | None = Field(alias="client_name#es-GT", title="Client name (Spanish (Guatemala))",
                                          default=None, placeholder="Client name (Spanish (Guatemala))")
    client_name_es_hn: str | None = Field(alias="client_name#es-HN", title="Client name (Spanish (Honduras))",
                                          default=None, placeholder="Client name (Spanish (Honduras))")
    client_name_es_mx: str | None = Field(alias="client_name#es-MX", title="Client name (Spanish (Mexico))",
                                          default=None, placeholder="Client name (Spanish (Mexico))")
    client_name_es_ni: str | None = Field(alias="client_name#es-NI", title="Client name (Spanish (Nicaragua))",
                                          default=None, placeholder="Client name (Spanish (Nicaragua))")
    client_name_es_pa: str | None = Field(alias="client_name#es-PA", title="Client name (Spanish (Panama))",
                                          default=None, placeholder="Client name (Spanish (Panama))")
    client_name_es_pe: str | None = Field(alias="client_name#es-PE", title="Client name (Spanish (Peru))", default=None,
                                          placeholder="Client name (Spanish (Peru))")
    client_name_es_pr: str | None = Field(alias="client_name#es-PR", title="Client name (Spanish (Puerto Rico))",
                                          default=None, placeholder="Client name (Spanish (Puerto Rico))")
    client_name_es_py: str | None = Field(alias="client_name#es-PY", title="Client name (Spanish (Paraguay))",
                                          default=None, placeholder="Client name (Spanish (Paraguay))")
    client_name_es_sv: str | None = Field(alias="client_name#es-SV", title="Client name (Spanish (El Salvador))",
                                          default=None, placeholder="Client name (Spanish (El Salvador))")
    client_name_es_uy: str | None = Field(alias="client_name#es-UY", title="Client name (Spanish (Uruguay))",
                                          default=None, placeholder="Client name (Spanish (Uruguay))")
    client_name_es_ve: str | None = Field(alias="client_name#es-VE", title="Client name (Spanish (Venezuela))",
                                          default=None, placeholder="Client name (Spanish (Venezuela))")
    client_name_et_ee: str | None = Field(alias="client_name#et-EE", title="Client name (Estonian (Estonia))",
                                          default=None, placeholder="Client name (Estonian (Estonia))")
    client_name_eu_es: str | None = Field(alias="client_name#eu-ES", title="Client name (Basque (Spain))", default=None,
                                          placeholder="Client name (Basque (Spain))")
    client_name_fa_ir: str | None = Field(alias="client_name#fa-IR", title="Client name (Farsi (Iran))", default=None,
                                          placeholder="Client name (Farsi (Iran))")
    client_name_fi_fi: str | None = Field(alias="client_name#fi-FI", title="Client name (Finnish (Finland))",
                                          default=None, placeholder="Client name (Finnish (Finland))")
    client_name_fo_fo: str | None = Field(alias="client_name#fo-FO", title="Client name (Faroese (Faroe Islands))",
                                          default=None, placeholder="Client name (Faroese (Faroe Islands))")
    client_name_fr_be: str | None = Field(alias="client_name#fr-BE", title="Client name (French (Belgium))",
                                          default=None, placeholder="Client name (French (Belgium))")
    client_name_fr_ca: str | None = Field(alias="client_name#fr-CA", title="Client name (French (Canada))",
                                          default=None, placeholder="Client name (French (Canada))")
    client_name_fr_ch: str | None = Field(alias="client_name#fr-CH", title="Client name (French (Switzerland))",
                                          default=None, placeholder="Client name (French (Switzerland))")
    client_name_fr_fr: str | None = Field(alias="client_name#fr-FR", title="Client name (French (France))",
                                          default=None, placeholder="Client name (French (France))")
    client_name_fr_lu: str | None = Field(alias="client_name#fr-LU", title="Client name (French (Luxembourg))",
                                          default=None, placeholder="Client name (French (Luxembourg))")
    client_name_fr_mc: str | None = Field(alias="client_name#fr-MC",
                                          title="Client name (French (Principality of Monaco))", default=None,
                                          placeholder="Client name (French (Principality of Monaco))")
    client_name_gl_es: str | None = Field(alias="client_name#gl-ES", title="Client name (Galician (Spain))",
                                          default=None, placeholder="Client name (Galician (Spain))")
    client_name_gu_in: str | None = Field(alias="client_name#gu-IN", title="Client name (Gujarati (India))",
                                          default=None, placeholder="Client name (Gujarati (India))")
    client_name_he_il: str | None = Field(alias="client_name#he-IL", title="Client name (Hebrew (Israel))",
                                          default=None, placeholder="Client name (Hebrew (Israel))")
    client_name_hi_in: str | None = Field(alias="client_name#hi-IN", title="Client name (Hindi (India))", default=None,
                                          placeholder="Client name (Hindi (India))")
    client_name_hr_ba: str | None = Field(alias="client_name#hr-BA",
                                          title="Client name (Croatian (Bosnia and Herzegovina))", default=None,
                                          placeholder="Client name (Croatian (Bosnia and Herzegovina))")
    client_name_hr_hr: str | None = Field(alias="client_name#hr-HR", title="Client name (Croatian (Croatia))",
                                          default=None, placeholder="Client name (Croatian (Croatia))")
    client_name_hu_hu: str | None = Field(alias="client_name#hu-HU", title="Client name (Hungarian (Hungary))",
                                          default=None, placeholder="Client name (Hungarian (Hungary))")
    client_name_hy_am: str | None = Field(alias="client_name#hy-AM", title="Client name (Armenian (Armenia))",
                                          default=None, placeholder="Client name (Armenian (Armenia))")
    client_name_id_id: str | None = Field(alias="client_name#id-ID", title="Client name (Indonesian (Indonesia))",
                                          default=None, placeholder="Client name (Indonesian (Indonesia))")
    client_name_is_is: str | None = Field(alias="client_name#is-IS", title="Client name (Icelandic (Iceland))",
                                          default=None, placeholder="Client name (Icelandic (Iceland))")
    client_name_it_ch: str | None = Field(alias="client_name#it-CH", title="Client name (Italian (Switzerland))",
                                          default=None, placeholder="Client name (Italian (Switzerland))")
    client_name_it_it: str | None = Field(alias="client_name#it-IT", title="Client name (Italian (Italy))",
                                          default=None, placeholder="Client name (Italian (Italy))")
    client_name_ja_jp: str | None = Field(alias="client_name#ja-JP", title="Client name (Japanese (Japan))",
                                          default=None, placeholder="Client name (Japanese (Japan))")
    client_name_ka_ge: str | None = Field(alias="client_name#ka-GE", title="Client name (Georgian (Georgia))",
                                          default=None, placeholder="Client name (Georgian (Georgia))")
    client_name_kk_kz: str | None = Field(alias="client_name#kk-KZ", title="Client name (Kazakh (Kazakhstan))",
                                          default=None, placeholder="Client name (Kazakh (Kazakhstan))")
    client_name_kn_in: str | None = Field(alias="client_name#kn-IN", title="Client name (Kannada (India))",
                                          default=None, placeholder="Client name (Kannada (India))")
    client_name_ko_kr: str | None = Field(alias="client_name#ko-KR", title="Client name (Korean (Korea))", default=None,
                                          placeholder="Client name (Korean (Korea))")
    client_name_kok_in: str | None = Field(alias="client_name#kok-IN", title="Client name (Konkani (India))",
                                           default=None, placeholder="Client name (Konkani (India))")
    client_name_ky_kg: str | None = Field(alias="client_name#ky-KG", title="Client name (Kyrgyz (Kyrgyzstan))",
                                          default=None, placeholder="Client name (Kyrgyz (Kyrgyzstan))")
    client_name_lt_lt: str | None = Field(alias="client_name#lt-LT", title="Client name (Lithuanian (Lithuania))",
                                          default=None, placeholder="Client name (Lithuanian (Lithuania))")
    client_name_lv_lv: str | None = Field(alias="client_name#lv-LV", title="Client name (Latvian (Latvia))",
                                          default=None, placeholder="Client name (Latvian (Latvia))")
    client_name_mi_nz: str | None = Field(alias="client_name#mi-NZ", title="Client name (Maori (New Zealand))",
                                          default=None, placeholder="Client name (Maori (New Zealand))")
    client_name_mk_mk: str | None = Field(alias="client_name#mk-MK",
                                          title="Client name (FYRO Macedonian (Former Yugoslav Republic of Macedonia))",
                                          default=None,
                                          placeholder="Client name (FYRO Macedonian (Former Yugoslav Republic of Macedonia))")
    client_name_mn_mn: str | None = Field(alias="client_name#mn-MN", title="Client name (Mongolian (Mongolia))",
                                          default=None, placeholder="Client name (Mongolian (Mongolia))")
    client_name_mr_in: str | None = Field(alias="client_name#mr-IN", title="Client name (Marathi (India))",
                                          default=None, placeholder="Client name (Marathi (India))")
    client_name_ms_bn: str | None = Field(alias="client_name#ms-BN", title="Client name (Malay (Brunei Darussalam))",
                                          default=None, placeholder="Client name (Malay (Brunei Darussalam))")
    client_name_ms_my: str | None = Field(alias="client_name#ms-MY", title="Client name (Malay (Malaysia))",
                                          default=None, placeholder="Client name (Malay (Malaysia))")
    client_name_mt_mt: str | None = Field(alias="client_name#mt-MT", title="Client name (Maltese (Malta))",
                                          default=None, placeholder="Client name (Maltese (Malta))")
    client_name_nb_no: str | None = Field(alias="client_name#nb-NO", title="Client name (Norwegian (Bokm?l) (Norway))",
                                          default=None, placeholder="Client name (Norwegian (Bokm?l) (Norway))")
    client_name_nl_be: str | None = Field(alias="client_name#nl-BE", title="Client name (Dutch (Belgium))",
                                          default=None, placeholder="Client name (Dutch (Belgium))")
    client_name_nl_nl: str | None = Field(alias="client_name#nl-NL", title="Client name (Dutch (Netherlands))",
                                          default=None, placeholder="Client name (Dutch (Netherlands))")
    client_name_nn_no: str | None = Field(alias="client_name#nn-NO", title="Client name (Norwegian (Nynorsk) (Norway))",
                                          default=None, placeholder="Client name (Norwegian (Nynorsk) (Norway))")
    client_name_ns_za: str | None = Field(alias="client_name#ns-ZA",
                                          title="Client name (Northern Sotho (South Africa))", default=None,
                                          placeholder="Client name (Northern Sotho (South Africa))")
    client_name_pa_in: str | None = Field(alias="client_name#pa-IN", title="Client name (Punjabi (India))",
                                          default=None, placeholder="Client name (Punjabi (India))")
    client_name_pl_pl: str | None = Field(alias="client_name#pl-PL", title="Client name (Polish (Poland))",
                                          default=None, placeholder="Client name (Polish (Poland))")
    client_name_ps_ar: str | None = Field(alias="client_name#ps-AR", title="Client name (Pashto (Afghanistan))",
                                          default=None, placeholder="Client name (Pashto (Afghanistan))")
    client_name_pt_br: str | None = Field(alias="client_name#pt-BR", title="Client name (Portuguese (Brazil))",
                                          default=None, placeholder="Client name (Portuguese (Brazil))")
    client_name_pt_pt: str | None = Field(alias="client_name#pt-PT", title="Client name (Portuguese (Portugal))",
                                          default=None, placeholder="Client name (Portuguese (Portugal))")
    client_name_qu_bo: str | None = Field(alias="client_name#qu-BO", title="Client name (Quechua (Bolivia))",
                                          default=None, placeholder="Client name (Quechua (Bolivia))")
    client_name_qu_ec: str | None = Field(alias="client_name#qu-EC", title="Client name (Quechua (Ecuador))",
                                          default=None, placeholder="Client name (Quechua (Ecuador))")
    client_name_qu_pe: str | None = Field(alias="client_name#qu-PE", title="Client name (Quechua (Peru))", default=None,
                                          placeholder="Client name (Quechua (Peru))")
    client_name_ro_ro: str | None = Field(alias="client_name#ro-RO", title="Client name (Romanian (Romania))",
                                          default=None, placeholder="Client name (Romanian (Romania))")
    client_name_ru_ru: str | None = Field(alias="client_name#ru-RU", title="Client name (Russian (Russia))",
                                          default=None, placeholder="Client name (Russian (Russia))")
    client_name_sa_in: str | None = Field(alias="client_name#sa-IN", title="Client name (Sanskrit (India))",
                                          default=None, placeholder="Client name (Sanskrit (India))")
    client_name_se_fi: str | None = Field(alias="client_name#se-FI", title="Client name (Sami (Finland))", default=None,
                                          placeholder="Client name (Sami (Finland))")
    client_name_se_no: str | None = Field(alias="client_name#se-NO", title="Client name (Sami (Norway))", default=None,
                                          placeholder="Client name (Sami (Norway))")
    client_name_se_se: str | None = Field(alias="client_name#se-SE", title="Client name (Sami (Sweden))", default=None,
                                          placeholder="Client name (Sami (Sweden))")
    client_name_sk_sk: str | None = Field(alias="client_name#sk-SK", title="Client name (Slovak (Slovakia))",
                                          default=None, placeholder="Client name (Slovak (Slovakia))")
    client_name_sl_si: str | None = Field(alias="client_name#sl-SI", title="Client name (Slovenian (Slovenia))",
                                          default=None, placeholder="Client name (Slovenian (Slovenia))")
    client_name_sq_al: str | None = Field(alias="client_name#sq-AL", title="Client name (Albanian (Albania))",
                                          default=None, placeholder="Client name (Albanian (Albania))")
    client_name_sr_ba: str | None = Field(alias="client_name#sr-BA",
                                          title="Client name (Serbian (Latin) (Bosnia and Herzegovina))", default=None,
                                          placeholder="Client name (Serbian (Latin) (Bosnia and Herzegovina))")
    client_name_sr_cyrl_ba: str | None = Field(alias="client_name#sr-Cyrl-BA",
                                               title="Client name (Serbian (Cyrillic) (Bosnia and Herzegovina))",
                                               default=None,
                                               placeholder="Client name (Serbian (Cyrillic) (Bosnia and Herzegovina))")
    client_name_sr_sp: str | None = Field(alias="client_name#sr-SP",
                                          title="Client name (Serbian (Latin) (Serbia and Montenegro))", default=None,
                                          placeholder="Client name (Serbian (Latin) (Serbia and Montenegro))")
    client_name_sr_cyrl_sp: str | None = Field(alias="client_name#sr-Cyrl-SP",
                                               title="Client name (Serbian (Cyrillic) (Serbia and Montenegro))",
                                               default=None,
                                               placeholder="Client name (Serbian (Cyrillic) (Serbia and Montenegro))")
    client_name_sv_fi: str | None = Field(alias="client_name#sv-FI", title="Client name (Swedish (Finland))",
                                          default=None, placeholder="Client name (Swedish (Finland))")
    client_name_sv_se: str | None = Field(alias="client_name#sv-SE", title="Client name (Swedish (Sweden))",
                                          default=None, placeholder="Client name (Swedish (Sweden))")
    client_name_sw_ke: str | None = Field(alias="client_name#sw-KE", title="Client name (Swahili (Kenya))",
                                          default=None, placeholder="Client name (Swahili (Kenya))")
    client_name_syr_sy: str | None = Field(alias="client_name#syr-SY", title="Client name (Syriac (Syria))",
                                           default=None, placeholder="Client name (Syriac (Syria))")
    client_name_ta_in: str | None = Field(alias="client_name#ta-IN", title="Client name (Tamil (India))", default=None,
                                          placeholder="Client name (Tamil (India))")
    client_name_te_in: str | None = Field(alias="client_name#te-IN", title="Client name (Telugu (India))", default=None,
                                          placeholder="Client name (Telugu (India))")
    client_name_th_th: str | None = Field(alias="client_name#th-TH", title="Client name (Thai (Thailand))",
                                          default=None, placeholder="Client name (Thai (Thailand))")
    client_name_tl_ph: str | None = Field(alias="client_name#tl-PH", title="Client name (Tagalog (Philippines))",
                                          default=None, placeholder="Client name (Tagalog (Philippines))")
    client_name_tn_za: str | None = Field(alias="client_name#tn-ZA", title="Client name (Tswana (South Africa))",
                                          default=None, placeholder="Client name (Tswana (South Africa))")
    client_name_tr_tr: str | None = Field(alias="client_name#tr-TR", title="Client name (Turkish (Turkey))",
                                          default=None, placeholder="Client name (Turkish (Turkey))")
    client_name_tt_ru: str | None = Field(alias="client_name#tt-RU", title="Client name (Tatar (Russia))", default=None,
                                          placeholder="Client name (Tatar (Russia))")
    client_name_uk_ua: str | None = Field(alias="client_name#uk-UA", title="Client name (Ukrainian (Ukraine))",
                                          default=None, placeholder="Client name (Ukrainian (Ukraine))")
    client_name_ur_pk: str | None = Field(alias="client_name#ur-PK",
                                          title="Client name (Urdu (Islamic Republic of Pakistan))", default=None,
                                          placeholder="Client name (Urdu (Islamic Republic of Pakistan))")
    client_name_uz_uz: str | None = Field(alias="client_name#uz-UZ", title="Client name (Uzbek (Latin) (Uzbekistan))",
                                          default=None, placeholder="Client name (Uzbek (Latin) (Uzbekistan))")
    client_name_uz_cyrl_uz: str | None = Field(alias="client_name#uz-Cyrl-UZ",
                                               title="Client name (Uzbek (Cyrillic) (Uzbekistan))", default=None,
                                               placeholder="Client name (Uzbek (Cyrillic) (Uzbekistan))")
    client_name_vi_vn: str | None = Field(alias="client_name#vi-VN", title="Client name (Vietnamese (Viet Nam))",
                                          default=None, placeholder="Client name (Vietnamese (Viet Nam))")
    client_name_xh_za: str | None = Field(alias="client_name#xh-ZA", title="Client name (Xhosa (South Africa))",
                                          default=None, placeholder="Client name (Xhosa (South Africa))")
    client_name_zh_cn: str | None = Field(alias="client_name#zh-CN", title="Client name (Chinese (S))", default=None,
                                          placeholder="Client name (Chinese (S))")
    client_name_zh_hk: str | None = Field(alias="client_name#zh-HK", title="Client name (Chinese (Hong Kong))",
                                          default=None, placeholder="Client name (Chinese (Hong Kong))")
    client_name_zh_mo: str | None = Field(alias="client_name#zh-MO", title="Client name (Chinese (Macau))",
                                          default=None, placeholder="Client name (Chinese (Macau))")
    client_name_zh_sg: str | None = Field(alias="client_name#zh-SG", title="Client name (Chinese (Singapore))",
                                          default=None, placeholder="Client name (Chinese (Singapore))")
    client_name_zh_tw: str | None = Field(alias="client_name#zh-TW", title="Client name (Chinese (T))", default=None,
                                          placeholder="Client name (Chinese (T))")
    client_name_zu_za: str | None = Field(alias="client_name#zu-ZA", title="Client name (Zulu (South Africa))",
                                          default=None, placeholder="Client name (Zulu (South Africa))")


class TOSURILangs(BaseModel):
    tos_uri_af_za: HttpsUrl | None = Field(alias="tos_uri#af-ZA", title="ToS URI (Afrikaans (South Africa))",
                                           default=None, placeholder="https://sub.example.com")
    tos_uri_ar_ae: HttpsUrl | None = Field(alias="tos_uri#ar-AE", title="ToS URI (Arabic (U.A.E.))", default=None,
                                           placeholder="https://sub.example.com")
    tos_uri_ar_bh: HttpsUrl | None = Field(alias="tos_uri#ar-BH", title="ToS URI (Arabic (Bahrain))", default=None,
                                           placeholder="https://sub.example.com")
    tos_uri_ar_dz: HttpsUrl | None = Field(alias="tos_uri#ar-DZ", title="ToS URI (Arabic (Algeria))", default=None,
                                           placeholder="https://sub.example.com")
    tos_uri_ar_eg: HttpsUrl | None = Field(alias="tos_uri#ar-EG", title="ToS URI (Arabic (Egypt))", default=None,
                                           placeholder="https://sub.example.com")
    tos_uri_ar_iq: HttpsUrl | None = Field(alias="tos_uri#ar-IQ", title="ToS URI (Arabic (Iraq))", default=None,
                                           placeholder="https://sub.example.com")
    tos_uri_ar_jo: HttpsUrl | None = Field(alias="tos_uri#ar-JO", title="ToS URI (Arabic (Jordan))", default=None,
                                           placeholder="https://sub.example.com")
    tos_uri_ar_kw: HttpsUrl | None = Field(alias="tos_uri#ar-KW", title="ToS URI (Arabic (Kuwait))", default=None,
                                           placeholder="https://sub.example.com")
    tos_uri_ar_lb: HttpsUrl | None = Field(alias="tos_uri#ar-LB", title="ToS URI (Arabic (Lebanon))", default=None,
                                           placeholder="https://sub.example.com")
    tos_uri_ar_ly: HttpsUrl | None = Field(alias="tos_uri#ar-LY", title="ToS URI (Arabic (Libya))", default=None,
                                           placeholder="https://sub.example.com")
    tos_uri_ar_ma: HttpsUrl | None = Field(alias="tos_uri#ar-MA", title="ToS URI (Arabic (Morocco))", default=None,
                                           placeholder="https://sub.example.com")
    tos_uri_ar_om: HttpsUrl | None = Field(alias="tos_uri#ar-OM", title="ToS URI (Arabic (Oman))", default=None,
                                           placeholder="https://sub.example.com")
    tos_uri_ar_qa: HttpsUrl | None = Field(alias="tos_uri#ar-QA", title="ToS URI (Arabic (Qatar))", default=None,
                                           placeholder="https://sub.example.com")
    tos_uri_ar_sa: HttpsUrl | None = Field(alias="tos_uri#ar-SA", title="ToS URI (Arabic (Saudi Arabia))", default=None,
                                           placeholder="https://sub.example.com")
    tos_uri_ar_sy: HttpsUrl | None = Field(alias="tos_uri#ar-SY", title="ToS URI (Arabic (Syria))", default=None,
                                           placeholder="https://sub.example.com")
    tos_uri_ar_tn: HttpsUrl | None = Field(alias="tos_uri#ar-TN", title="ToS URI (Arabic (Tunisia))", default=None,
                                           placeholder="https://sub.example.com")
    tos_uri_ar_ye: HttpsUrl | None = Field(alias="tos_uri#ar-YE", title="ToS URI (Arabic (Yemen))", default=None,
                                           placeholder="https://sub.example.com")
    tos_uri_az_az: HttpsUrl | None = Field(alias="tos_uri#az-AZ", title="ToS URI (Azeri (Latin) (Azerbaijan))",
                                           default=None, placeholder="https://sub.example.com")
    tos_uri_az_cyrl_az: HttpsUrl | None = Field(alias="tos_uri#az-Cyrl-AZ",
                                                title="ToS URI (Azeri (Cyrillic) (Azerbaijan))", default=None,
                                                placeholder="https://sub.example.com")
    tos_uri_be_by: HttpsUrl | None = Field(alias="tos_uri#be-BY", title="ToS URI (Belarusian (Belarus))", default=None,
                                           placeholder="https://sub.example.com")
    tos_uri_bg_bg: HttpsUrl | None = Field(alias="tos_uri#bg-BG", title="ToS URI (Bulgarian (Bulgaria))", default=None,
                                           placeholder="https://sub.example.com")
    tos_uri_bs_ba: HttpsUrl | None = Field(alias="tos_uri#bs-BA", title="ToS URI (Bosnian (Bosnia and Herzegovina))",
                                           default=None, placeholder="https://sub.example.com")
    tos_uri_ca_es: HttpsUrl | None = Field(alias="tos_uri#ca-ES", title="ToS URI (Catalan (Spain))", default=None,
                                           placeholder="https://sub.example.com")
    tos_uri_cs_cz: HttpsUrl | None = Field(alias="tos_uri#cs-CZ", title="ToS URI (Czech (Czech Republic))",
                                           default=None, placeholder="https://sub.example.com")
    tos_uri_cy_gb: HttpsUrl | None = Field(alias="tos_uri#cy-GB", title="ToS URI (Welsh (United Kingdom))",
                                           default=None, placeholder="https://sub.example.com")
    tos_uri_da_dk: HttpsUrl | None = Field(alias="tos_uri#da-DK", title="ToS URI (Danish (Denmark))", default=None,
                                           placeholder="https://sub.example.com")
    tos_uri_de_at: HttpsUrl | None = Field(alias="tos_uri#de-AT", title="ToS URI (German (Austria))", default=None,
                                           placeholder="https://sub.example.com")
    tos_uri_de_ch: HttpsUrl | None = Field(alias="tos_uri#de-CH", title="ToS URI (German (Switzerland))", default=None,
                                           placeholder="https://sub.example.com")
    tos_uri_de_de: HttpsUrl | None = Field(alias="tos_uri#de-DE", title="ToS URI (German (Germany))", default=None,
                                           placeholder="https://sub.example.com")
    tos_uri_de_li: HttpsUrl | None = Field(alias="tos_uri#de-LI", title="ToS URI (German (Liechtenstein))",
                                           default=None, placeholder="https://sub.example.com")
    tos_uri_de_lu: HttpsUrl | None = Field(alias="tos_uri#de-LU", title="ToS URI (German (Luxembourg))", default=None,
                                           placeholder="https://sub.example.com")
    tos_uri_dv_mv: HttpsUrl | None = Field(alias="tos_uri#dv-MV", title="ToS URI (Divehi (Maldives))", default=None,
                                           placeholder="https://sub.example.com")
    tos_uri_el_gr: HttpsUrl | None = Field(alias="tos_uri#el-GR", title="ToS URI (Greek (Greece))", default=None,
                                           placeholder="https://sub.example.com")
    tos_uri_en_au: HttpsUrl | None = Field(alias="tos_uri#en-AU", title="ToS URI (English (Australia))", default=None,
                                           placeholder="https://sub.example.com")
    tos_uri_en_bz: HttpsUrl | None = Field(alias="tos_uri#en-BZ", title="ToS URI (English (Belize))", default=None,
                                           placeholder="https://sub.example.com")
    tos_uri_en_ca: HttpsUrl | None = Field(alias="tos_uri#en-CA", title="ToS URI (English (Canada))", default=None,
                                           placeholder="https://sub.example.com")
    tos_uri_en_cb: HttpsUrl | None = Field(alias="tos_uri#en-CB", title="ToS URI (English (Caribbean))", default=None,
                                           placeholder="https://sub.example.com")
    tos_uri_en_gb: HttpsUrl | None = Field(alias="tos_uri#en-GB", title="ToS URI (English (United Kingdom))",
                                           default=None, placeholder="https://sub.example.com")
    tos_uri_en_ie: HttpsUrl | None = Field(alias="tos_uri#en-IE", title="ToS URI (English (Ireland))", default=None,
                                           placeholder="https://sub.example.com")
    tos_uri_en_jm: HttpsUrl | None = Field(alias="tos_uri#en-JM", title="ToS URI (English (Jamaica))", default=None,
                                           placeholder="https://sub.example.com")
    tos_uri_en_nz: HttpsUrl | None = Field(alias="tos_uri#en-NZ", title="ToS URI (English (New Zealand))", default=None,
                                           placeholder="https://sub.example.com")
    tos_uri_en_ph: HttpsUrl | None = Field(alias="tos_uri#en-PH",
                                           title="ToS URI (English (Republic of the Philippines))", default=None,
                                           placeholder="https://sub.example.com")
    tos_uri_en_tt: HttpsUrl | None = Field(alias="tos_uri#en-TT", title="ToS URI (English (Trinidad and Tobago))",
                                           default=None, placeholder="https://sub.example.com")
    tos_uri_en_us: HttpsUrl | None = Field(alias="tos_uri#en-US", title="ToS URI (English (United States))",
                                           default=None, placeholder="https://sub.example.com")
    tos_uri_en_za: HttpsUrl | None = Field(alias="tos_uri#en-ZA", title="ToS URI (English (South Africa))",
                                           default=None, placeholder="https://sub.example.com")
    tos_uri_en_zw: HttpsUrl | None = Field(alias="tos_uri#en-ZW", title="ToS URI (English (Zimbabwe))", default=None,
                                           placeholder="https://sub.example.com")
    tos_uri_es_ar: HttpsUrl | None = Field(alias="tos_uri#es-AR", title="ToS URI (Spanish (Argentina))", default=None,
                                           placeholder="https://sub.example.com")
    tos_uri_es_bo: HttpsUrl | None = Field(alias="tos_uri#es-BO", title="ToS URI (Spanish (Bolivia))", default=None,
                                           placeholder="https://sub.example.com")
    tos_uri_es_cl: HttpsUrl | None = Field(alias="tos_uri#es-CL", title="ToS URI (Spanish (Chile))", default=None,
                                           placeholder="https://sub.example.com")
    tos_uri_es_co: HttpsUrl | None = Field(alias="tos_uri#es-CO", title="ToS URI (Spanish (Colombia))", default=None,
                                           placeholder="https://sub.example.com")
    tos_uri_es_cr: HttpsUrl | None = Field(alias="tos_uri#es-CR", title="ToS URI (Spanish (Costa Rica))", default=None,
                                           placeholder="https://sub.example.com")
    tos_uri_es_do: HttpsUrl | None = Field(alias="tos_uri#es-DO", title="ToS URI (Spanish (Dominican Republic))",
                                           default=None, placeholder="https://sub.example.com")
    tos_uri_es_ec: HttpsUrl | None = Field(alias="tos_uri#es-EC", title="ToS URI (Spanish (Ecuador))", default=None,
                                           placeholder="https://sub.example.com")
    tos_uri_es_es: HttpsUrl | None = Field(alias="tos_uri#es-ES", title="ToS URI (Spanish (Spain))", default=None,
                                           placeholder="https://sub.example.com")
    tos_uri_es_gt: HttpsUrl | None = Field(alias="tos_uri#es-GT", title="ToS URI (Spanish (Guatemala))", default=None,
                                           placeholder="https://sub.example.com")
    tos_uri_es_hn: HttpsUrl | None = Field(alias="tos_uri#es-HN", title="ToS URI (Spanish (Honduras))", default=None,
                                           placeholder="https://sub.example.com")
    tos_uri_es_mx: HttpsUrl | None = Field(alias="tos_uri#es-MX", title="ToS URI (Spanish (Mexico))", default=None,
                                           placeholder="https://sub.example.com")
    tos_uri_es_ni: HttpsUrl | None = Field(alias="tos_uri#es-NI", title="ToS URI (Spanish (Nicaragua))", default=None,
                                           placeholder="https://sub.example.com")
    tos_uri_es_pa: HttpsUrl | None = Field(alias="tos_uri#es-PA", title="ToS URI (Spanish (Panama))", default=None,
                                           placeholder="https://sub.example.com")
    tos_uri_es_pe: HttpsUrl | None = Field(alias="tos_uri#es-PE", title="ToS URI (Spanish (Peru))", default=None,
                                           placeholder="https://sub.example.com")
    tos_uri_es_pr: HttpsUrl | None = Field(alias="tos_uri#es-PR", title="ToS URI (Spanish (Puerto Rico))", default=None,
                                           placeholder="https://sub.example.com")
    tos_uri_es_py: HttpsUrl | None = Field(alias="tos_uri#es-PY", title="ToS URI (Spanish (Paraguay))", default=None,
                                           placeholder="https://sub.example.com")
    tos_uri_es_sv: HttpsUrl | None = Field(alias="tos_uri#es-SV", title="ToS URI (Spanish (El Salvador))", default=None,
                                           placeholder="https://sub.example.com")
    tos_uri_es_uy: HttpsUrl | None = Field(alias="tos_uri#es-UY", title="ToS URI (Spanish (Uruguay))", default=None,
                                           placeholder="https://sub.example.com")
    tos_uri_es_ve: HttpsUrl | None = Field(alias="tos_uri#es-VE", title="ToS URI (Spanish (Venezuela))", default=None,
                                           placeholder="https://sub.example.com")
    tos_uri_et_ee: HttpsUrl | None = Field(alias="tos_uri#et-EE", title="ToS URI (Estonian (Estonia))", default=None,
                                           placeholder="https://sub.example.com")
    tos_uri_eu_es: HttpsUrl | None = Field(alias="tos_uri#eu-ES", title="ToS URI (Basque (Spain))", default=None,
                                           placeholder="https://sub.example.com")
    tos_uri_fa_ir: HttpsUrl | None = Field(alias="tos_uri#fa-IR", title="ToS URI (Farsi (Iran))", default=None,
                                           placeholder="https://sub.example.com")
    tos_uri_fi_fi: HttpsUrl | None = Field(alias="tos_uri#fi-FI", title="ToS URI (Finnish (Finland))", default=None,
                                           placeholder="https://sub.example.com")
    tos_uri_fo_fo: HttpsUrl | None = Field(alias="tos_uri#fo-FO", title="ToS URI (Faroese (Faroe Islands))",
                                           default=None, placeholder="https://sub.example.com")
    tos_uri_fr_be: HttpsUrl | None = Field(alias="tos_uri#fr-BE", title="ToS URI (French (Belgium))", default=None,
                                           placeholder="https://sub.example.com")
    tos_uri_fr_ca: HttpsUrl | None = Field(alias="tos_uri#fr-CA", title="ToS URI (French (Canada))", default=None,
                                           placeholder="https://sub.example.com")
    tos_uri_fr_ch: HttpsUrl | None = Field(alias="tos_uri#fr-CH", title="ToS URI (French (Switzerland))", default=None,
                                           placeholder="https://sub.example.com")
    tos_uri_fr_fr: HttpsUrl | None = Field(alias="tos_uri#fr-FR", title="ToS URI (French (France))", default=None,
                                           placeholder="https://sub.example.com")
    tos_uri_fr_lu: HttpsUrl | None = Field(alias="tos_uri#fr-LU", title="ToS URI (French (Luxembourg))", default=None,
                                           placeholder="https://sub.example.com")
    tos_uri_fr_mc: HttpsUrl | None = Field(alias="tos_uri#fr-MC", title="ToS URI (French (Principality of Monaco))",
                                           default=None, placeholder="https://sub.example.com")
    tos_uri_gl_es: HttpsUrl | None = Field(alias="tos_uri#gl-ES", title="ToS URI (Galician (Spain))", default=None,
                                           placeholder="https://sub.example.com")
    tos_uri_gu_in: HttpsUrl | None = Field(alias="tos_uri#gu-IN", title="ToS URI (Gujarati (India))", default=None,
                                           placeholder="https://sub.example.com")
    tos_uri_he_il: HttpsUrl | None = Field(alias="tos_uri#he-IL", title="ToS URI (Hebrew (Israel))", default=None,
                                           placeholder="https://sub.example.com")
    tos_uri_hi_in: HttpsUrl | None = Field(alias="tos_uri#hi-IN", title="ToS URI (Hindi (India))", default=None,
                                           placeholder="https://sub.example.com")
    tos_uri_hr_ba: HttpsUrl | None = Field(alias="tos_uri#hr-BA", title="ToS URI (Croatian (Bosnia and Herzegovina))",
                                           default=None, placeholder="https://sub.example.com")
    tos_uri_hr_hr: HttpsUrl | None = Field(alias="tos_uri#hr-HR", title="ToS URI (Croatian (Croatia))", default=None,
                                           placeholder="https://sub.example.com")
    tos_uri_hu_hu: HttpsUrl | None = Field(alias="tos_uri#hu-HU", title="ToS URI (Hungarian (Hungary))", default=None,
                                           placeholder="https://sub.example.com")
    tos_uri_hy_am: HttpsUrl | None = Field(alias="tos_uri#hy-AM", title="ToS URI (Armenian (Armenia))", default=None,
                                           placeholder="https://sub.example.com")
    tos_uri_id_id: HttpsUrl | None = Field(alias="tos_uri#id-ID", title="ToS URI (Indonesian (Indonesia))",
                                           default=None, placeholder="https://sub.example.com")
    tos_uri_is_is: HttpsUrl | None = Field(alias="tos_uri#is-IS", title="ToS URI (Icelandic (Iceland))", default=None,
                                           placeholder="https://sub.example.com")
    tos_uri_it_ch: HttpsUrl | None = Field(alias="tos_uri#it-CH", title="ToS URI (Italian (Switzerland))", default=None,
                                           placeholder="https://sub.example.com")
    tos_uri_it_it: HttpsUrl | None = Field(alias="tos_uri#it-IT", title="ToS URI (Italian (Italy))", default=None,
                                           placeholder="https://sub.example.com")
    tos_uri_ja_jp: HttpsUrl | None = Field(alias="tos_uri#ja-JP", title="ToS URI (Japanese (Japan))", default=None,
                                           placeholder="https://sub.example.com")
    tos_uri_ka_ge: HttpsUrl | None = Field(alias="tos_uri#ka-GE", title="ToS URI (Georgian (Georgia))", default=None,
                                           placeholder="https://sub.example.com")
    tos_uri_kk_kz: HttpsUrl | None = Field(alias="tos_uri#kk-KZ", title="ToS URI (Kazakh (Kazakhstan))", default=None,
                                           placeholder="https://sub.example.com")
    tos_uri_kn_in: HttpsUrl | None = Field(alias="tos_uri#kn-IN", title="ToS URI (Kannada (India))", default=None,
                                           placeholder="https://sub.example.com")
    tos_uri_ko_kr: HttpsUrl | None = Field(alias="tos_uri#ko-KR", title="ToS URI (Korean (Korea))", default=None,
                                           placeholder="https://sub.example.com")
    tos_uri_kok_in: HttpsUrl | None = Field(alias="tos_uri#kok-IN", title="ToS URI (Konkani (India))", default=None,
                                            placeholder="https://sub.example.com")
    tos_uri_ky_kg: HttpsUrl | None = Field(alias="tos_uri#ky-KG", title="ToS URI (Kyrgyz (Kyrgyzstan))", default=None,
                                           placeholder="https://sub.example.com")
    tos_uri_lt_lt: HttpsUrl | None = Field(alias="tos_uri#lt-LT", title="ToS URI (Lithuanian (Lithuania))",
                                           default=None, placeholder="https://sub.example.com")
    tos_uri_lv_lv: HttpsUrl | None = Field(alias="tos_uri#lv-LV", title="ToS URI (Latvian (Latvia))", default=None,
                                           placeholder="https://sub.example.com")
    tos_uri_mi_nz: HttpsUrl | None = Field(alias="tos_uri#mi-NZ", title="ToS URI (Maori (New Zealand))", default=None,
                                           placeholder="https://sub.example.com")
    tos_uri_mk_mk: HttpsUrl | None = Field(alias="tos_uri#mk-MK",
                                           title="ToS URI (FYRO Macedonian (Former Yugoslav Republic of Macedonia))",
                                           default=None, placeholder="https://sub.example.com")
    tos_uri_mn_mn: HttpsUrl | None = Field(alias="tos_uri#mn-MN", title="ToS URI (Mongolian (Mongolia))", default=None,
                                           placeholder="https://sub.example.com")
    tos_uri_mr_in: HttpsUrl | None = Field(alias="tos_uri#mr-IN", title="ToS URI (Marathi (India))", default=None,
                                           placeholder="https://sub.example.com")
    tos_uri_ms_bn: HttpsUrl | None = Field(alias="tos_uri#ms-BN", title="ToS URI (Malay (Brunei Darussalam))",
                                           default=None, placeholder="https://sub.example.com")
    tos_uri_ms_my: HttpsUrl | None = Field(alias="tos_uri#ms-MY", title="ToS URI (Malay (Malaysia))", default=None,
                                           placeholder="https://sub.example.com")
    tos_uri_mt_mt: HttpsUrl | None = Field(alias="tos_uri#mt-MT", title="ToS URI (Maltese (Malta))", default=None,
                                           placeholder="https://sub.example.com")
    tos_uri_nb_no: HttpsUrl | None = Field(alias="tos_uri#nb-NO", title="ToS URI (Norwegian (Bokm?l) (Norway))",
                                           default=None, placeholder="https://sub.example.com")
    tos_uri_nl_be: HttpsUrl | None = Field(alias="tos_uri#nl-BE", title="ToS URI (Dutch (Belgium))", default=None,
                                           placeholder="https://sub.example.com")
    tos_uri_nl_nl: HttpsUrl | None = Field(alias="tos_uri#nl-NL", title="ToS URI (Dutch (Netherlands))", default=None,
                                           placeholder="https://sub.example.com")
    tos_uri_nn_no: HttpsUrl | None = Field(alias="tos_uri#nn-NO", title="ToS URI (Norwegian (Nynorsk) (Norway))",
                                           default=None, placeholder="https://sub.example.com")
    tos_uri_ns_za: HttpsUrl | None = Field(alias="tos_uri#ns-ZA", title="ToS URI (Northern Sotho (South Africa))",
                                           default=None, placeholder="https://sub.example.com")
    tos_uri_pa_in: HttpsUrl | None = Field(alias="tos_uri#pa-IN", title="ToS URI (Punjabi (India))", default=None,
                                           placeholder="https://sub.example.com")
    tos_uri_pl_pl: HttpsUrl | None = Field(alias="tos_uri#pl-PL", title="ToS URI (Polish (Poland))", default=None,
                                           placeholder="https://sub.example.com")
    tos_uri_ps_ar: HttpsUrl | None = Field(alias="tos_uri#ps-AR", title="ToS URI (Pashto (Afghanistan))", default=None,
                                           placeholder="https://sub.example.com")
    tos_uri_pt_br: HttpsUrl | None = Field(alias="tos_uri#pt-BR", title="ToS URI (Portuguese (Brazil))", default=None,
                                           placeholder="https://sub.example.com")
    tos_uri_pt_pt: HttpsUrl | None = Field(alias="tos_uri#pt-PT", title="ToS URI (Portuguese (Portugal))", default=None,
                                           placeholder="https://sub.example.com")
    tos_uri_qu_bo: HttpsUrl | None = Field(alias="tos_uri#qu-BO", title="ToS URI (Quechua (Bolivia))", default=None,
                                           placeholder="https://sub.example.com")
    tos_uri_qu_ec: HttpsUrl | None = Field(alias="tos_uri#qu-EC", title="ToS URI (Quechua (Ecuador))", default=None,
                                           placeholder="https://sub.example.com")
    tos_uri_qu_pe: HttpsUrl | None = Field(alias="tos_uri#qu-PE", title="ToS URI (Quechua (Peru))", default=None,
                                           placeholder="https://sub.example.com")
    tos_uri_ro_ro: HttpsUrl | None = Field(alias="tos_uri#ro-RO", title="ToS URI (Romanian (Romania))", default=None,
                                           placeholder="https://sub.example.com")
    tos_uri_ru_ru: HttpsUrl | None = Field(alias="tos_uri#ru-RU", title="ToS URI (Russian (Russia))", default=None,
                                           placeholder="https://sub.example.com")
    tos_uri_sa_in: HttpsUrl | None = Field(alias="tos_uri#sa-IN", title="ToS URI (Sanskrit (India))", default=None,
                                           placeholder="https://sub.example.com")
    tos_uri_se_fi: HttpsUrl | None = Field(alias="tos_uri#se-FI", title="ToS URI (Sami (Finland))", default=None,
                                           placeholder="https://sub.example.com")
    tos_uri_se_no: HttpsUrl | None = Field(alias="tos_uri#se-NO", title="ToS URI (Sami (Norway))", default=None,
                                           placeholder="https://sub.example.com")
    tos_uri_se_se: HttpsUrl | None = Field(alias="tos_uri#se-SE", title="ToS URI (Sami (Sweden))", default=None,
                                           placeholder="https://sub.example.com")
    tos_uri_sk_sk: HttpsUrl | None = Field(alias="tos_uri#sk-SK", title="ToS URI (Slovak (Slovakia))", default=None,
                                           placeholder="https://sub.example.com")
    tos_uri_sl_si: HttpsUrl | None = Field(alias="tos_uri#sl-SI", title="ToS URI (Slovenian (Slovenia))", default=None,
                                           placeholder="https://sub.example.com")
    tos_uri_sq_al: HttpsUrl | None = Field(alias="tos_uri#sq-AL", title="ToS URI (Albanian (Albania))", default=None,
                                           placeholder="https://sub.example.com")
    tos_uri_sr_ba: HttpsUrl | None = Field(alias="tos_uri#sr-BA",
                                           title="ToS URI (Serbian (Latin) (Bosnia and Herzegovina))", default=None,
                                           placeholder="https://sub.example.com")
    tos_uri_sr_cyrl_ba: HttpsUrl | None = Field(alias="tos_uri#sr-Cyrl-BA",
                                                title="ToS URI (Serbian (Cyrillic) (Bosnia and Herzegovina))",
                                                default=None, placeholder="https://sub.example.com")
    tos_uri_sr_sp: HttpsUrl | None = Field(alias="tos_uri#sr-SP",
                                           title="ToS URI (Serbian (Latin) (Serbia and Montenegro))", default=None,
                                           placeholder="https://sub.example.com")
    tos_uri_sr_cyrl_sp: HttpsUrl | None = Field(alias="tos_uri#sr-Cyrl-SP",
                                                title="ToS URI (Serbian (Cyrillic) (Serbia and Montenegro))",
                                                default=None, placeholder="https://sub.example.com")
    tos_uri_sv_fi: HttpsUrl | None = Field(alias="tos_uri#sv-FI", title="ToS URI (Swedish (Finland))", default=None,
                                           placeholder="https://sub.example.com")
    tos_uri_sv_se: HttpsUrl | None = Field(alias="tos_uri#sv-SE", title="ToS URI (Swedish (Sweden))", default=None,
                                           placeholder="https://sub.example.com")
    tos_uri_sw_ke: HttpsUrl | None = Field(alias="tos_uri#sw-KE", title="ToS URI (Swahili (Kenya))", default=None,
                                           placeholder="https://sub.example.com")
    tos_uri_syr_sy: HttpsUrl | None = Field(alias="tos_uri#syr-SY", title="ToS URI (Syriac (Syria))", default=None,
                                            placeholder="https://sub.example.com")
    tos_uri_ta_in: HttpsUrl | None = Field(alias="tos_uri#ta-IN", title="ToS URI (Tamil (India))", default=None,
                                           placeholder="https://sub.example.com")
    tos_uri_te_in: HttpsUrl | None = Field(alias="tos_uri#te-IN", title="ToS URI (Telugu (India))", default=None,
                                           placeholder="https://sub.example.com")
    tos_uri_th_th: HttpsUrl | None = Field(alias="tos_uri#th-TH", title="ToS URI (Thai (Thailand))", default=None,
                                           placeholder="https://sub.example.com")
    tos_uri_tl_ph: HttpsUrl | None = Field(alias="tos_uri#tl-PH", title="ToS URI (Tagalog (Philippines))", default=None,
                                           placeholder="https://sub.example.com")
    tos_uri_tn_za: HttpsUrl | None = Field(alias="tos_uri#tn-ZA", title="ToS URI (Tswana (South Africa))", default=None,
                                           placeholder="https://sub.example.com")
    tos_uri_tr_tr: HttpsUrl | None = Field(alias="tos_uri#tr-TR", title="ToS URI (Turkish (Turkey))", default=None,
                                           placeholder="https://sub.example.com")
    tos_uri_tt_ru: HttpsUrl | None = Field(alias="tos_uri#tt-RU", title="ToS URI (Tatar (Russia))", default=None,
                                           placeholder="https://sub.example.com")
    tos_uri_uk_ua: HttpsUrl | None = Field(alias="tos_uri#uk-UA", title="ToS URI (Ukrainian (Ukraine))", default=None,
                                           placeholder="https://sub.example.com")
    tos_uri_ur_pk: HttpsUrl | None = Field(alias="tos_uri#ur-PK", title="ToS URI (Urdu (Islamic Republic of Pakistan))",
                                           default=None, placeholder="https://sub.example.com")
    tos_uri_uz_uz: HttpsUrl | None = Field(alias="tos_uri#uz-UZ", title="ToS URI (Uzbek (Latin) (Uzbekistan))",
                                           default=None, placeholder="https://sub.example.com")
    tos_uri_uz_cyrl_uz: HttpsUrl | None = Field(alias="tos_uri#uz-Cyrl-UZ",
                                                title="ToS URI (Uzbek (Cyrillic) (Uzbekistan))", default=None,
                                                placeholder="https://sub.example.com")
    tos_uri_vi_vn: HttpsUrl | None = Field(alias="tos_uri#vi-VN", title="ToS URI (Vietnamese (Viet Nam))", default=None,
                                           placeholder="https://sub.example.com")
    tos_uri_xh_za: HttpsUrl | None = Field(alias="tos_uri#xh-ZA", title="ToS URI (Xhosa (South Africa))", default=None,
                                           placeholder="https://sub.example.com")
    tos_uri_zh_cn: HttpsUrl | None = Field(alias="tos_uri#zh-CN", title="ToS URI (Chinese (S))", default=None,
                                           placeholder="https://sub.example.com")
    tos_uri_zh_hk: HttpsUrl | None = Field(alias="tos_uri#zh-HK", title="ToS URI (Chinese (Hong Kong))", default=None,
                                           placeholder="https://sub.example.com")
    tos_uri_zh_mo: HttpsUrl | None = Field(alias="tos_uri#zh-MO", title="ToS URI (Chinese (Macau))", default=None,
                                           placeholder="https://sub.example.com")
    tos_uri_zh_sg: HttpsUrl | None = Field(alias="tos_uri#zh-SG", title="ToS URI (Chinese (Singapore))", default=None,
                                           placeholder="https://sub.example.com")
    tos_uri_zh_tw: HttpsUrl | None = Field(alias="tos_uri#zh-TW", title="ToS URI (Chinese (T))", default=None,
                                           placeholder="https://sub.example.com")
    tos_uri_zu_za: HttpsUrl | None = Field(alias="tos_uri#zu-ZA", title="ToS URI (Zulu (South Africa))", default=None,
                                           placeholder="https://sub.example.com")


class PolicyURILangs(BaseModel):
    policy_uri_af_za: HttpsUrl | None = Field(alias="policy_uri#af-ZA", title="Policy URI (Afrikaans (South Africa))",
                                              default=None, placeholder="https://sub.example.com")
    policy_uri_ar_ae: HttpsUrl | None = Field(alias="policy_uri#ar-AE", title="Policy URI (Arabic (U.A.E.))",
                                              default=None, placeholder="https://sub.example.com")
    policy_uri_ar_bh: HttpsUrl | None = Field(alias="policy_uri#ar-BH", title="Policy URI (Arabic (Bahrain))",
                                              default=None, placeholder="https://sub.example.com")
    policy_uri_ar_dz: HttpsUrl | None = Field(alias="policy_uri#ar-DZ", title="Policy URI (Arabic (Algeria))",
                                              default=None, placeholder="https://sub.example.com")
    policy_uri_ar_eg: HttpsUrl | None = Field(alias="policy_uri#ar-EG", title="Policy URI (Arabic (Egypt))",
                                              default=None, placeholder="https://sub.example.com")
    policy_uri_ar_iq: HttpsUrl | None = Field(alias="policy_uri#ar-IQ", title="Policy URI (Arabic (Iraq))",
                                              default=None, placeholder="https://sub.example.com")
    policy_uri_ar_jo: HttpsUrl | None = Field(alias="policy_uri#ar-JO", title="Policy URI (Arabic (Jordan))",
                                              default=None, placeholder="https://sub.example.com")
    policy_uri_ar_kw: HttpsUrl | None = Field(alias="policy_uri#ar-KW", title="Policy URI (Arabic (Kuwait))",
                                              default=None, placeholder="https://sub.example.com")
    policy_uri_ar_lb: HttpsUrl | None = Field(alias="policy_uri#ar-LB", title="Policy URI (Arabic (Lebanon))",
                                              default=None, placeholder="https://sub.example.com")
    policy_uri_ar_ly: HttpsUrl | None = Field(alias="policy_uri#ar-LY", title="Policy URI (Arabic (Libya))",
                                              default=None, placeholder="https://sub.example.com")
    policy_uri_ar_ma: HttpsUrl | None = Field(alias="policy_uri#ar-MA", title="Policy URI (Arabic (Morocco))",
                                              default=None, placeholder="https://sub.example.com")
    policy_uri_ar_om: HttpsUrl | None = Field(alias="policy_uri#ar-OM", title="Policy URI (Arabic (Oman))",
                                              default=None, placeholder="https://sub.example.com")
    policy_uri_ar_qa: HttpsUrl | None = Field(alias="policy_uri#ar-QA", title="Policy URI (Arabic (Qatar))",
                                              default=None, placeholder="https://sub.example.com")
    policy_uri_ar_sa: HttpsUrl | None = Field(alias="policy_uri#ar-SA", title="Policy URI (Arabic (Saudi Arabia))",
                                              default=None, placeholder="https://sub.example.com")
    policy_uri_ar_sy: HttpsUrl | None = Field(alias="policy_uri#ar-SY", title="Policy URI (Arabic (Syria))",
                                              default=None, placeholder="https://sub.example.com")
    policy_uri_ar_tn: HttpsUrl | None = Field(alias="policy_uri#ar-TN", title="Policy URI (Arabic (Tunisia))",
                                              default=None, placeholder="https://sub.example.com")
    policy_uri_ar_ye: HttpsUrl | None = Field(alias="policy_uri#ar-YE", title="Policy URI (Arabic (Yemen))",
                                              default=None, placeholder="https://sub.example.com")
    policy_uri_az_az: HttpsUrl | None = Field(alias="policy_uri#az-AZ", title="Policy URI (Azeri (Latin) (Azerbaijan))",
                                              default=None, placeholder="https://sub.example.com")
    policy_uri_az_cyrl_az: HttpsUrl | None = Field(alias="policy_uri#az-Cyrl-AZ",
                                                   title="Policy URI (Azeri (Cyrillic) (Azerbaijan))", default=None,
                                                   placeholder="https://sub.example.com")
    policy_uri_be_by: HttpsUrl | None = Field(alias="policy_uri#be-BY", title="Policy URI (Belarusian (Belarus))",
                                              default=None, placeholder="https://sub.example.com")
    policy_uri_bg_bg: HttpsUrl | None = Field(alias="policy_uri#bg-BG", title="Policy URI (Bulgarian (Bulgaria))",
                                              default=None, placeholder="https://sub.example.com")
    policy_uri_bs_ba: HttpsUrl | None = Field(alias="policy_uri#bs-BA",
                                              title="Policy URI (Bosnian (Bosnia and Herzegovina))", default=None,
                                              placeholder="https://sub.example.com")
    policy_uri_ca_es: HttpsUrl | None = Field(alias="policy_uri#ca-ES", title="Policy URI (Catalan (Spain))",
                                              default=None, placeholder="https://sub.example.com")
    policy_uri_cs_cz: HttpsUrl | None = Field(alias="policy_uri#cs-CZ", title="Policy URI (Czech (Czech Republic))",
                                              default=None, placeholder="https://sub.example.com")
    policy_uri_cy_gb: HttpsUrl | None = Field(alias="policy_uri#cy-GB", title="Policy URI (Welsh (United Kingdom))",
                                              default=None, placeholder="https://sub.example.com")
    policy_uri_da_dk: HttpsUrl | None = Field(alias="policy_uri#da-DK", title="Policy URI (Danish (Denmark))",
                                              default=None, placeholder="https://sub.example.com")
    policy_uri_de_at: HttpsUrl | None = Field(alias="policy_uri#de-AT", title="Policy URI (German (Austria))",
                                              default=None, placeholder="https://sub.example.com")
    policy_uri_de_ch: HttpsUrl | None = Field(alias="policy_uri#de-CH", title="Policy URI (German (Switzerland))",
                                              default=None, placeholder="https://sub.example.com")
    policy_uri_de_de: HttpsUrl | None = Field(alias="policy_uri#de-DE", title="Policy URI (German (Germany))",
                                              default=None, placeholder="https://sub.example.com")
    policy_uri_de_li: HttpsUrl | None = Field(alias="policy_uri#de-LI", title="Policy URI (German (Liechtenstein))",
                                              default=None, placeholder="https://sub.example.com")
    policy_uri_de_lu: HttpsUrl | None = Field(alias="policy_uri#de-LU", title="Policy URI (German (Luxembourg))",
                                              default=None, placeholder="https://sub.example.com")
    policy_uri_dv_mv: HttpsUrl | None = Field(alias="policy_uri#dv-MV", title="Policy URI (Divehi (Maldives))",
                                              default=None, placeholder="https://sub.example.com")
    policy_uri_el_gr: HttpsUrl | None = Field(alias="policy_uri#el-GR", title="Policy URI (Greek (Greece))",
                                              default=None, placeholder="https://sub.example.com")
    policy_uri_en_au: HttpsUrl | None = Field(alias="policy_uri#en-AU", title="Policy URI (English (Australia))",
                                              default=None, placeholder="https://sub.example.com")
    policy_uri_en_bz: HttpsUrl | None = Field(alias="policy_uri#en-BZ", title="Policy URI (English (Belize))",
                                              default=None, placeholder="https://sub.example.com")
    policy_uri_en_ca: HttpsUrl | None = Field(alias="policy_uri#en-CA", title="Policy URI (English (Canada))",
                                              default=None, placeholder="https://sub.example.com")
    policy_uri_en_cb: HttpsUrl | None = Field(alias="policy_uri#en-CB", title="Policy URI (English (Caribbean))",
                                              default=None, placeholder="https://sub.example.com")
    policy_uri_en_gb: HttpsUrl | None = Field(alias="policy_uri#en-GB", title="Policy URI (English (United Kingdom))",
                                              default=None, placeholder="https://sub.example.com")
    policy_uri_en_ie: HttpsUrl | None = Field(alias="policy_uri#en-IE", title="Policy URI (English (Ireland))",
                                              default=None, placeholder="https://sub.example.com")
    policy_uri_en_jm: HttpsUrl | None = Field(alias="policy_uri#en-JM", title="Policy URI (English (Jamaica))",
                                              default=None, placeholder="https://sub.example.com")
    policy_uri_en_nz: HttpsUrl | None = Field(alias="policy_uri#en-NZ", title="Policy URI (English (New Zealand))",
                                              default=None, placeholder="https://sub.example.com")
    policy_uri_en_ph: HttpsUrl | None = Field(alias="policy_uri#en-PH",
                                              title="Policy URI (English (Republic of the Philippines))", default=None,
                                              placeholder="https://sub.example.com")
    policy_uri_en_tt: HttpsUrl | None = Field(alias="policy_uri#en-TT",
                                              title="Policy URI (English (Trinidad and Tobago))", default=None,
                                              placeholder="https://sub.example.com")
    policy_uri_en_us: HttpsUrl | None = Field(alias="policy_uri#en-US", title="Policy URI (English (United States))",
                                              default=None, placeholder="https://sub.example.com")
    policy_uri_en_za: HttpsUrl | None = Field(alias="policy_uri#en-ZA", title="Policy URI (English (South Africa))",
                                              default=None, placeholder="https://sub.example.com")
    policy_uri_en_zw: HttpsUrl | None = Field(alias="policy_uri#en-ZW", title="Policy URI (English (Zimbabwe))",
                                              default=None, placeholder="https://sub.example.com")
    policy_uri_es_ar: HttpsUrl | None = Field(alias="policy_uri#es-AR", title="Policy URI (Spanish (Argentina))",
                                              default=None, placeholder="https://sub.example.com")
    policy_uri_es_bo: HttpsUrl | None = Field(alias="policy_uri#es-BO", title="Policy URI (Spanish (Bolivia))",
                                              default=None, placeholder="https://sub.example.com")
    policy_uri_es_cl: HttpsUrl | None = Field(alias="policy_uri#es-CL", title="Policy URI (Spanish (Chile))",
                                              default=None, placeholder="https://sub.example.com")
    policy_uri_es_co: HttpsUrl | None = Field(alias="policy_uri#es-CO", title="Policy URI (Spanish (Colombia))",
                                              default=None, placeholder="https://sub.example.com")
    policy_uri_es_cr: HttpsUrl | None = Field(alias="policy_uri#es-CR", title="Policy URI (Spanish (Costa Rica))",
                                              default=None, placeholder="https://sub.example.com")
    policy_uri_es_do: HttpsUrl | None = Field(alias="policy_uri#es-DO",
                                              title="Policy URI (Spanish (Dominican Republic))", default=None,
                                              placeholder="https://sub.example.com")
    policy_uri_es_ec: HttpsUrl | None = Field(alias="policy_uri#es-EC", title="Policy URI (Spanish (Ecuador))",
                                              default=None, placeholder="https://sub.example.com")
    policy_uri_es_es: HttpsUrl | None = Field(alias="policy_uri#es-ES", title="Policy URI (Spanish (Spain))",
                                              default=None, placeholder="https://sub.example.com")
    policy_uri_es_gt: HttpsUrl | None = Field(alias="policy_uri#es-GT", title="Policy URI (Spanish (Guatemala))",
                                              default=None, placeholder="https://sub.example.com")
    policy_uri_es_hn: HttpsUrl | None = Field(alias="policy_uri#es-HN", title="Policy URI (Spanish (Honduras))",
                                              default=None, placeholder="https://sub.example.com")
    policy_uri_es_mx: HttpsUrl | None = Field(alias="policy_uri#es-MX", title="Policy URI (Spanish (Mexico))",
                                              default=None, placeholder="https://sub.example.com")
    policy_uri_es_ni: HttpsUrl | None = Field(alias="policy_uri#es-NI", title="Policy URI (Spanish (Nicaragua))",
                                              default=None, placeholder="https://sub.example.com")
    policy_uri_es_pa: HttpsUrl | None = Field(alias="policy_uri#es-PA", title="Policy URI (Spanish (Panama))",
                                              default=None, placeholder="https://sub.example.com")
    policy_uri_es_pe: HttpsUrl | None = Field(alias="policy_uri#es-PE", title="Policy URI (Spanish (Peru))",
                                              default=None, placeholder="https://sub.example.com")
    policy_uri_es_pr: HttpsUrl | None = Field(alias="policy_uri#es-PR", title="Policy URI (Spanish (Puerto Rico))",
                                              default=None, placeholder="https://sub.example.com")
    policy_uri_es_py: HttpsUrl | None = Field(alias="policy_uri#es-PY", title="Policy URI (Spanish (Paraguay))",
                                              default=None, placeholder="https://sub.example.com")
    policy_uri_es_sv: HttpsUrl | None = Field(alias="policy_uri#es-SV", title="Policy URI (Spanish (El Salvador))",
                                              default=None, placeholder="https://sub.example.com")
    policy_uri_es_uy: HttpsUrl | None = Field(alias="policy_uri#es-UY", title="Policy URI (Spanish (Uruguay))",
                                              default=None, placeholder="https://sub.example.com")
    policy_uri_es_ve: HttpsUrl | None = Field(alias="policy_uri#es-VE", title="Policy URI (Spanish (Venezuela))",
                                              default=None, placeholder="https://sub.example.com")
    policy_uri_et_ee: HttpsUrl | None = Field(alias="policy_uri#et-EE", title="Policy URI (Estonian (Estonia))",
                                              default=None, placeholder="https://sub.example.com")
    policy_uri_eu_es: HttpsUrl | None = Field(alias="policy_uri#eu-ES", title="Policy URI (Basque (Spain))",
                                              default=None, placeholder="https://sub.example.com")
    policy_uri_fa_ir: HttpsUrl | None = Field(alias="policy_uri#fa-IR", title="Policy URI (Farsi (Iran))", default=None,
                                              placeholder="https://sub.example.com")
    policy_uri_fi_fi: HttpsUrl | None = Field(alias="policy_uri#fi-FI", title="Policy URI (Finnish (Finland))",
                                              default=None, placeholder="https://sub.example.com")
    policy_uri_fo_fo: HttpsUrl | None = Field(alias="policy_uri#fo-FO", title="Policy URI (Faroese (Faroe Islands))",
                                              default=None, placeholder="https://sub.example.com")
    policy_uri_fr_be: HttpsUrl | None = Field(alias="policy_uri#fr-BE", title="Policy URI (French (Belgium))",
                                              default=None, placeholder="https://sub.example.com")
    policy_uri_fr_ca: HttpsUrl | None = Field(alias="policy_uri#fr-CA", title="Policy URI (French (Canada))",
                                              default=None, placeholder="https://sub.example.com")
    policy_uri_fr_ch: HttpsUrl | None = Field(alias="policy_uri#fr-CH", title="Policy URI (French (Switzerland))",
                                              default=None, placeholder="https://sub.example.com")
    policy_uri_fr_fr: HttpsUrl | None = Field(alias="policy_uri#fr-FR", title="Policy URI (French (France))",
                                              default=None, placeholder="https://sub.example.com")
    policy_uri_fr_lu: HttpsUrl | None = Field(alias="policy_uri#fr-LU", title="Policy URI (French (Luxembourg))",
                                              default=None, placeholder="https://sub.example.com")
    policy_uri_fr_mc: HttpsUrl | None = Field(alias="policy_uri#fr-MC",
                                              title="Policy URI (French (Principality of Monaco))", default=None,
                                              placeholder="https://sub.example.com")
    policy_uri_gl_es: HttpsUrl | None = Field(alias="policy_uri#gl-ES", title="Policy URI (Galician (Spain))",
                                              default=None, placeholder="https://sub.example.com")
    policy_uri_gu_in: HttpsUrl | None = Field(alias="policy_uri#gu-IN", title="Policy URI (Gujarati (India))",
                                              default=None, placeholder="https://sub.example.com")
    policy_uri_he_il: HttpsUrl | None = Field(alias="policy_uri#he-IL", title="Policy URI (Hebrew (Israel))",
                                              default=None, placeholder="https://sub.example.com")
    policy_uri_hi_in: HttpsUrl | None = Field(alias="policy_uri#hi-IN", title="Policy URI (Hindi (India))",
                                              default=None, placeholder="https://sub.example.com")
    policy_uri_hr_ba: HttpsUrl | None = Field(alias="policy_uri#hr-BA",
                                              title="Policy URI (Croatian (Bosnia and Herzegovina))", default=None,
                                              placeholder="https://sub.example.com")
    policy_uri_hr_hr: HttpsUrl | None = Field(alias="policy_uri#hr-HR", title="Policy URI (Croatian (Croatia))",
                                              default=None, placeholder="https://sub.example.com")
    policy_uri_hu_hu: HttpsUrl | None = Field(alias="policy_uri#hu-HU", title="Policy URI (Hungarian (Hungary))",
                                              default=None, placeholder="https://sub.example.com")
    policy_uri_hy_am: HttpsUrl | None = Field(alias="policy_uri#hy-AM", title="Policy URI (Armenian (Armenia))",
                                              default=None, placeholder="https://sub.example.com")
    policy_uri_id_id: HttpsUrl | None = Field(alias="policy_uri#id-ID", title="Policy URI (Indonesian (Indonesia))",
                                              default=None, placeholder="https://sub.example.com")
    policy_uri_is_is: HttpsUrl | None = Field(alias="policy_uri#is-IS", title="Policy URI (Icelandic (Iceland))",
                                              default=None, placeholder="https://sub.example.com")
    policy_uri_it_ch: HttpsUrl | None = Field(alias="policy_uri#it-CH", title="Policy URI (Italian (Switzerland))",
                                              default=None, placeholder="https://sub.example.com")
    policy_uri_it_it: HttpsUrl | None = Field(alias="policy_uri#it-IT", title="Policy URI (Italian (Italy))",
                                              default=None, placeholder="https://sub.example.com")
    policy_uri_ja_jp: HttpsUrl | None = Field(alias="policy_uri#ja-JP", title="Policy URI (Japanese (Japan))",
                                              default=None, placeholder="https://sub.example.com")
    policy_uri_ka_ge: HttpsUrl | None = Field(alias="policy_uri#ka-GE", title="Policy URI (Georgian (Georgia))",
                                              default=None, placeholder="https://sub.example.com")
    policy_uri_kk_kz: HttpsUrl | None = Field(alias="policy_uri#kk-KZ", title="Policy URI (Kazakh (Kazakhstan))",
                                              default=None, placeholder="https://sub.example.com")
    policy_uri_kn_in: HttpsUrl | None = Field(alias="policy_uri#kn-IN", title="Policy URI (Kannada (India))",
                                              default=None, placeholder="https://sub.example.com")
    policy_uri_ko_kr: HttpsUrl | None = Field(alias="policy_uri#ko-KR", title="Policy URI (Korean (Korea))",
                                              default=None, placeholder="https://sub.example.com")
    policy_uri_kok_in: HttpsUrl | None = Field(alias="policy_uri#kok-IN", title="Policy URI (Konkani (India))",
                                               default=None, placeholder="https://sub.example.com")
    policy_uri_ky_kg: HttpsUrl | None = Field(alias="policy_uri#ky-KG", title="Policy URI (Kyrgyz (Kyrgyzstan))",
                                              default=None, placeholder="https://sub.example.com")
    policy_uri_lt_lt: HttpsUrl | None = Field(alias="policy_uri#lt-LT", title="Policy URI (Lithuanian (Lithuania))",
                                              default=None, placeholder="https://sub.example.com")
    policy_uri_lv_lv: HttpsUrl | None = Field(alias="policy_uri#lv-LV", title="Policy URI (Latvian (Latvia))",
                                              default=None, placeholder="https://sub.example.com")
    policy_uri_mi_nz: HttpsUrl | None = Field(alias="policy_uri#mi-NZ", title="Policy URI (Maori (New Zealand))",
                                              default=None, placeholder="https://sub.example.com")
    policy_uri_mk_mk: HttpsUrl | None = Field(alias="policy_uri#mk-MK",
                                              title="Policy URI (FYRO Macedonian (Former Yugoslav Republic of Macedonia))",
                                              default=None, placeholder="https://sub.example.com")
    policy_uri_mn_mn: HttpsUrl | None = Field(alias="policy_uri#mn-MN", title="Policy URI (Mongolian (Mongolia))",
                                              default=None, placeholder="https://sub.example.com")
    policy_uri_mr_in: HttpsUrl | None = Field(alias="policy_uri#mr-IN", title="Policy URI (Marathi (India))",
                                              default=None, placeholder="https://sub.example.com")
    policy_uri_ms_bn: HttpsUrl | None = Field(alias="policy_uri#ms-BN", title="Policy URI (Malay (Brunei Darussalam))",
                                              default=None, placeholder="https://sub.example.com")
    policy_uri_ms_my: HttpsUrl | None = Field(alias="policy_uri#ms-MY", title="Policy URI (Malay (Malaysia))",
                                              default=None, placeholder="https://sub.example.com")
    policy_uri_mt_mt: HttpsUrl | None = Field(alias="policy_uri#mt-MT", title="Policy URI (Maltese (Malta))",
                                              default=None, placeholder="https://sub.example.com")
    policy_uri_nb_no: HttpsUrl | None = Field(alias="policy_uri#nb-NO",
                                              title="Policy URI (Norwegian (Bokm?l) (Norway))", default=None,
                                              placeholder="https://sub.example.com")
    policy_uri_nl_be: HttpsUrl | None = Field(alias="policy_uri#nl-BE", title="Policy URI (Dutch (Belgium))",
                                              default=None, placeholder="https://sub.example.com")
    policy_uri_nl_nl: HttpsUrl | None = Field(alias="policy_uri#nl-NL", title="Policy URI (Dutch (Netherlands))",
                                              default=None, placeholder="https://sub.example.com")
    policy_uri_nn_no: HttpsUrl | None = Field(alias="policy_uri#nn-NO",
                                              title="Policy URI (Norwegian (Nynorsk) (Norway))", default=None,
                                              placeholder="https://sub.example.com")
    policy_uri_ns_za: HttpsUrl | None = Field(alias="policy_uri#ns-ZA",
                                              title="Policy URI (Northern Sotho (South Africa))", default=None,
                                              placeholder="https://sub.example.com")
    policy_uri_pa_in: HttpsUrl | None = Field(alias="policy_uri#pa-IN", title="Policy URI (Punjabi (India))",
                                              default=None, placeholder="https://sub.example.com")
    policy_uri_pl_pl: HttpsUrl | None = Field(alias="policy_uri#pl-PL", title="Policy URI (Polish (Poland))",
                                              default=None, placeholder="https://sub.example.com")
    policy_uri_ps_ar: HttpsUrl | None = Field(alias="policy_uri#ps-AR", title="Policy URI (Pashto (Afghanistan))",
                                              default=None, placeholder="https://sub.example.com")
    policy_uri_pt_br: HttpsUrl | None = Field(alias="policy_uri#pt-BR", title="Policy URI (Portuguese (Brazil))",
                                              default=None, placeholder="https://sub.example.com")
    policy_uri_pt_pt: HttpsUrl | None = Field(alias="policy_uri#pt-PT", title="Policy URI (Portuguese (Portugal))",
                                              default=None, placeholder="https://sub.example.com")
    policy_uri_qu_bo: HttpsUrl | None = Field(alias="policy_uri#qu-BO", title="Policy URI (Quechua (Bolivia))",
                                              default=None, placeholder="https://sub.example.com")
    policy_uri_qu_ec: HttpsUrl | None = Field(alias="policy_uri#qu-EC", title="Policy URI (Quechua (Ecuador))",
                                              default=None, placeholder="https://sub.example.com")
    policy_uri_qu_pe: HttpsUrl | None = Field(alias="policy_uri#qu-PE", title="Policy URI (Quechua (Peru))",
                                              default=None, placeholder="https://sub.example.com")
    policy_uri_ro_ro: HttpsUrl | None = Field(alias="policy_uri#ro-RO", title="Policy URI (Romanian (Romania))",
                                              default=None, placeholder="https://sub.example.com")
    policy_uri_ru_ru: HttpsUrl | None = Field(alias="policy_uri#ru-RU", title="Policy URI (Russian (Russia))",
                                              default=None, placeholder="https://sub.example.com")
    policy_uri_sa_in: HttpsUrl | None = Field(alias="policy_uri#sa-IN", title="Policy URI (Sanskrit (India))",
                                              default=None, placeholder="https://sub.example.com")
    policy_uri_se_fi: HttpsUrl | None = Field(alias="policy_uri#se-FI", title="Policy URI (Sami (Finland))",
                                              default=None, placeholder="https://sub.example.com")
    policy_uri_se_no: HttpsUrl | None = Field(alias="policy_uri#se-NO", title="Policy URI (Sami (Norway))",
                                              default=None, placeholder="https://sub.example.com")
    policy_uri_se_se: HttpsUrl | None = Field(alias="policy_uri#se-SE", title="Policy URI (Sami (Sweden))",
                                              default=None, placeholder="https://sub.example.com")
    policy_uri_sk_sk: HttpsUrl | None = Field(alias="policy_uri#sk-SK", title="Policy URI (Slovak (Slovakia))",
                                              default=None, placeholder="https://sub.example.com")
    policy_uri_sl_si: HttpsUrl | None = Field(alias="policy_uri#sl-SI", title="Policy URI (Slovenian (Slovenia))",
                                              default=None, placeholder="https://sub.example.com")
    policy_uri_sq_al: HttpsUrl | None = Field(alias="policy_uri#sq-AL", title="Policy URI (Albanian (Albania))",
                                              default=None, placeholder="https://sub.example.com")
    policy_uri_sr_ba: HttpsUrl | None = Field(alias="policy_uri#sr-BA",
                                              title="Policy URI (Serbian (Latin) (Bosnia and Herzegovina))",
                                              default=None, placeholder="https://sub.example.com")
    policy_uri_sr_cyrl_ba: HttpsUrl | None = Field(alias="policy_uri#sr-Cyrl-BA",
                                                   title="Policy URI (Serbian (Cyrillic) (Bosnia and Herzegovina))",
                                                   default=None, placeholder="https://sub.example.com")
    policy_uri_sr_sp: HttpsUrl | None = Field(alias="policy_uri#sr-SP",
                                              title="Policy URI (Serbian (Latin) (Serbia and Montenegro))",
                                              default=None, placeholder="https://sub.example.com")
    policy_uri_sr_cyrl_sp: HttpsUrl | None = Field(alias="policy_uri#sr-Cyrl-SP",
                                                   title="Policy URI (Serbian (Cyrillic) (Serbia and Montenegro))",
                                                   default=None, placeholder="https://sub.example.com")
    policy_uri_sv_fi: HttpsUrl | None = Field(alias="policy_uri#sv-FI", title="Policy URI (Swedish (Finland))",
                                              default=None, placeholder="https://sub.example.com")
    policy_uri_sv_se: HttpsUrl | None = Field(alias="policy_uri#sv-SE", title="Policy URI (Swedish (Sweden))",
                                              default=None, placeholder="https://sub.example.com")
    policy_uri_sw_ke: HttpsUrl | None = Field(alias="policy_uri#sw-KE", title="Policy URI (Swahili (Kenya))",
                                              default=None, placeholder="https://sub.example.com")
    policy_uri_syr_sy: HttpsUrl | None = Field(alias="policy_uri#syr-SY", title="Policy URI (Syriac (Syria))",
                                               default=None, placeholder="https://sub.example.com")
    policy_uri_ta_in: HttpsUrl | None = Field(alias="policy_uri#ta-IN", title="Policy URI (Tamil (India))",
                                              default=None, placeholder="https://sub.example.com")
    policy_uri_te_in: HttpsUrl | None = Field(alias="policy_uri#te-IN", title="Policy URI (Telugu (India))",
                                              default=None, placeholder="https://sub.example.com")
    policy_uri_th_th: HttpsUrl | None = Field(alias="policy_uri#th-TH", title="Policy URI (Thai (Thailand))",
                                              default=None, placeholder="https://sub.example.com")
    policy_uri_tl_ph: HttpsUrl | None = Field(alias="policy_uri#tl-PH", title="Policy URI (Tagalog (Philippines))",
                                              default=None, placeholder="https://sub.example.com")
    policy_uri_tn_za: HttpsUrl | None = Field(alias="policy_uri#tn-ZA", title="Policy URI (Tswana (South Africa))",
                                              default=None, placeholder="https://sub.example.com")
    policy_uri_tr_tr: HttpsUrl | None = Field(alias="policy_uri#tr-TR", title="Policy URI (Turkish (Turkey))",
                                              default=None, placeholder="https://sub.example.com")
    policy_uri_tt_ru: HttpsUrl | None = Field(alias="policy_uri#tt-RU", title="Policy URI (Tatar (Russia))",
                                              default=None, placeholder="https://sub.example.com")
    policy_uri_uk_ua: HttpsUrl | None = Field(alias="policy_uri#uk-UA", title="Policy URI (Ukrainian (Ukraine))",
                                              default=None, placeholder="https://sub.example.com")
    policy_uri_ur_pk: HttpsUrl | None = Field(alias="policy_uri#ur-PK",
                                              title="Policy URI (Urdu (Islamic Republic of Pakistan))", default=None,
                                              placeholder="https://sub.example.com")
    policy_uri_uz_uz: HttpsUrl | None = Field(alias="policy_uri#uz-UZ", title="Policy URI (Uzbek (Latin) (Uzbekistan))",
                                              default=None, placeholder="https://sub.example.com")
    policy_uri_uz_cyrl_uz: HttpsUrl | None = Field(alias="policy_uri#uz-Cyrl-UZ",
                                                   title="Policy URI (Uzbek (Cyrillic) (Uzbekistan))", default=None,
                                                   placeholder="https://sub.example.com")
    policy_uri_vi_vn: HttpsUrl | None = Field(alias="policy_uri#vi-VN", title="Policy URI (Vietnamese (Viet Nam))",
                                              default=None, placeholder="https://sub.example.com")
    policy_uri_xh_za: HttpsUrl | None = Field(alias="policy_uri#xh-ZA", title="Policy URI (Xhosa (South Africa))",
                                              default=None, placeholder="https://sub.example.com")
    policy_uri_zh_cn: HttpsUrl | None = Field(alias="policy_uri#zh-CN", title="Policy URI (Chinese (S))", default=None,
                                              placeholder="https://sub.example.com")
    policy_uri_zh_hk: HttpsUrl | None = Field(alias="policy_uri#zh-HK", title="Policy URI (Chinese (Hong Kong))",
                                              default=None, placeholder="https://sub.example.com")
    policy_uri_zh_mo: HttpsUrl | None = Field(alias="policy_uri#zh-MO", title="Policy URI (Chinese (Macau))",
                                              default=None, placeholder="https://sub.example.com")
    policy_uri_zh_sg: HttpsUrl | None = Field(alias="policy_uri#zh-SG", title="Policy URI (Chinese (Singapore))",
                                              default=None, placeholder="https://sub.example.com")
    policy_uri_zh_tw: HttpsUrl | None = Field(alias="policy_uri#zh-TW", title="Policy URI (Chinese (T))", default=None,
                                              placeholder="https://sub.example.com")
    policy_uri_zu_za: HttpsUrl | None = Field(alias="policy_uri#zu-ZA", title="Policy URI (Zulu (South Africa))",
                                              default=None, placeholder="https://sub.example.com")


class LogoURILangs(BaseModel):
    logo_uri_af_za: HttpsUrl | None = Field(alias="logo_uri#af-ZA", title="Logo URI (Afrikaans (South Africa))",
                                            default=None, placeholder="https://sub.example.com")
    logo_uri_ar_ae: HttpsUrl | None = Field(alias="logo_uri#ar-AE", title="Logo URI (Arabic (U.A.E.))", default=None,
                                            placeholder="https://sub.example.com")
    logo_uri_ar_bh: HttpsUrl | None = Field(alias="logo_uri#ar-BH", title="Logo URI (Arabic (Bahrain))", default=None,
                                            placeholder="https://sub.example.com")
    logo_uri_ar_dz: HttpsUrl | None = Field(alias="logo_uri#ar-DZ", title="Logo URI (Arabic (Algeria))", default=None,
                                            placeholder="https://sub.example.com")
    logo_uri_ar_eg: HttpsUrl | None = Field(alias="logo_uri#ar-EG", title="Logo URI (Arabic (Egypt))", default=None,
                                            placeholder="https://sub.example.com")
    logo_uri_ar_iq: HttpsUrl | None = Field(alias="logo_uri#ar-IQ", title="Logo URI (Arabic (Iraq))", default=None,
                                            placeholder="https://sub.example.com")
    logo_uri_ar_jo: HttpsUrl | None = Field(alias="logo_uri#ar-JO", title="Logo URI (Arabic (Jordan))", default=None,
                                            placeholder="https://sub.example.com")
    logo_uri_ar_kw: HttpsUrl | None = Field(alias="logo_uri#ar-KW", title="Logo URI (Arabic (Kuwait))", default=None,
                                            placeholder="https://sub.example.com")
    logo_uri_ar_lb: HttpsUrl | None = Field(alias="logo_uri#ar-LB", title="Logo URI (Arabic (Lebanon))", default=None,
                                            placeholder="https://sub.example.com")
    logo_uri_ar_ly: HttpsUrl | None = Field(alias="logo_uri#ar-LY", title="Logo URI (Arabic (Libya))", default=None,
                                            placeholder="https://sub.example.com")
    logo_uri_ar_ma: HttpsUrl | None = Field(alias="logo_uri#ar-MA", title="Logo URI (Arabic (Morocco))", default=None,
                                            placeholder="https://sub.example.com")
    logo_uri_ar_om: HttpsUrl | None = Field(alias="logo_uri#ar-OM", title="Logo URI (Arabic (Oman))", default=None,
                                            placeholder="https://sub.example.com")
    logo_uri_ar_qa: HttpsUrl | None = Field(alias="logo_uri#ar-QA", title="Logo URI (Arabic (Qatar))", default=None,
                                            placeholder="https://sub.example.com")
    logo_uri_ar_sa: HttpsUrl | None = Field(alias="logo_uri#ar-SA", title="Logo URI (Arabic (Saudi Arabia))",
                                            default=None, placeholder="https://sub.example.com")
    logo_uri_ar_sy: HttpsUrl | None = Field(alias="logo_uri#ar-SY", title="Logo URI (Arabic (Syria))", default=None,
                                            placeholder="https://sub.example.com")
    logo_uri_ar_tn: HttpsUrl | None = Field(alias="logo_uri#ar-TN", title="Logo URI (Arabic (Tunisia))", default=None,
                                            placeholder="https://sub.example.com")
    logo_uri_ar_ye: HttpsUrl | None = Field(alias="logo_uri#ar-YE", title="Logo URI (Arabic (Yemen))", default=None,
                                            placeholder="https://sub.example.com")
    logo_uri_az_az: HttpsUrl | None = Field(alias="logo_uri#az-AZ", title="Logo URI (Azeri (Latin) (Azerbaijan))",
                                            default=None, placeholder="https://sub.example.com")
    logo_uri_az_cyrl_az: HttpsUrl | None = Field(alias="logo_uri#az-Cyrl-AZ",
                                                 title="Logo URI (Azeri (Cyrillic) (Azerbaijan))", default=None,
                                                 placeholder="https://sub.example.com")
    logo_uri_be_by: HttpsUrl | None = Field(alias="logo_uri#be-BY", title="Logo URI (Belarusian (Belarus))",
                                            default=None, placeholder="https://sub.example.com")
    logo_uri_bg_bg: HttpsUrl | None = Field(alias="logo_uri#bg-BG", title="Logo URI (Bulgarian (Bulgaria))",
                                            default=None, placeholder="https://sub.example.com")
    logo_uri_bs_ba: HttpsUrl | None = Field(alias="logo_uri#bs-BA", title="Logo URI (Bosnian (Bosnia and Herzegovina))",
                                            default=None, placeholder="https://sub.example.com")
    logo_uri_ca_es: HttpsUrl | None = Field(alias="logo_uri#ca-ES", title="Logo URI (Catalan (Spain))", default=None,
                                            placeholder="https://sub.example.com")
    logo_uri_cs_cz: HttpsUrl | None = Field(alias="logo_uri#cs-CZ", title="Logo URI (Czech (Czech Republic))",
                                            default=None, placeholder="https://sub.example.com")
    logo_uri_cy_gb: HttpsUrl | None = Field(alias="logo_uri#cy-GB", title="Logo URI (Welsh (United Kingdom))",
                                            default=None, placeholder="https://sub.example.com")
    logo_uri_da_dk: HttpsUrl | None = Field(alias="logo_uri#da-DK", title="Logo URI (Danish (Denmark))", default=None,
                                            placeholder="https://sub.example.com")
    logo_uri_de_at: HttpsUrl | None = Field(alias="logo_uri#de-AT", title="Logo URI (German (Austria))", default=None,
                                            placeholder="https://sub.example.com")
    logo_uri_de_ch: HttpsUrl | None = Field(alias="logo_uri#de-CH", title="Logo URI (German (Switzerland))",
                                            default=None, placeholder="https://sub.example.com")
    logo_uri_de_de: HttpsUrl | None = Field(alias="logo_uri#de-DE", title="Logo URI (German (Germany))", default=None,
                                            placeholder="https://sub.example.com")
    logo_uri_de_li: HttpsUrl | None = Field(alias="logo_uri#de-LI", title="Logo URI (German (Liechtenstein))",
                                            default=None, placeholder="https://sub.example.com")
    logo_uri_de_lu: HttpsUrl | None = Field(alias="logo_uri#de-LU", title="Logo URI (German (Luxembourg))",
                                            default=None, placeholder="https://sub.example.com")
    logo_uri_dv_mv: HttpsUrl | None = Field(alias="logo_uri#dv-MV", title="Logo URI (Divehi (Maldives))", default=None,
                                            placeholder="https://sub.example.com")
    logo_uri_el_gr: HttpsUrl | None = Field(alias="logo_uri#el-GR", title="Logo URI (Greek (Greece))", default=None,
                                            placeholder="https://sub.example.com")
    logo_uri_en_au: HttpsUrl | None = Field(alias="logo_uri#en-AU", title="Logo URI (English (Australia))",
                                            default=None, placeholder="https://sub.example.com")
    logo_uri_en_bz: HttpsUrl | None = Field(alias="logo_uri#en-BZ", title="Logo URI (English (Belize))", default=None,
                                            placeholder="https://sub.example.com")
    logo_uri_en_ca: HttpsUrl | None = Field(alias="logo_uri#en-CA", title="Logo URI (English (Canada))", default=None,
                                            placeholder="https://sub.example.com")
    logo_uri_en_cb: HttpsUrl | None = Field(alias="logo_uri#en-CB", title="Logo URI (English (Caribbean))",
                                            default=None, placeholder="https://sub.example.com")
    logo_uri_en_gb: HttpsUrl | None = Field(alias="logo_uri#en-GB", title="Logo URI (English (United Kingdom))",
                                            default=None, placeholder="https://sub.example.com")
    logo_uri_en_ie: HttpsUrl | None = Field(alias="logo_uri#en-IE", title="Logo URI (English (Ireland))", default=None,
                                            placeholder="https://sub.example.com")
    logo_uri_en_jm: HttpsUrl | None = Field(alias="logo_uri#en-JM", title="Logo URI (English (Jamaica))", default=None,
                                            placeholder="https://sub.example.com")
    logo_uri_en_nz: HttpsUrl | None = Field(alias="logo_uri#en-NZ", title="Logo URI (English (New Zealand))",
                                            default=None, placeholder="https://sub.example.com")
    logo_uri_en_ph: HttpsUrl | None = Field(alias="logo_uri#en-PH",
                                            title="Logo URI (English (Republic of the Philippines))", default=None,
                                            placeholder="https://sub.example.com")
    logo_uri_en_tt: HttpsUrl | None = Field(alias="logo_uri#en-TT", title="Logo URI (English (Trinidad and Tobago))",
                                            default=None, placeholder="https://sub.example.com")
    logo_uri_en_us: HttpsUrl | None = Field(alias="logo_uri#en-US", title="Logo URI (English (United States))",
                                            default=None, placeholder="https://sub.example.com")
    logo_uri_en_za: HttpsUrl | None = Field(alias="logo_uri#en-ZA", title="Logo URI (English (South Africa))",
                                            default=None, placeholder="https://sub.example.com")
    logo_uri_en_zw: HttpsUrl | None = Field(alias="logo_uri#en-ZW", title="Logo URI (English (Zimbabwe))", default=None,
                                            placeholder="https://sub.example.com")
    logo_uri_es_ar: HttpsUrl | None = Field(alias="logo_uri#es-AR", title="Logo URI (Spanish (Argentina))",
                                            default=None, placeholder="https://sub.example.com")
    logo_uri_es_bo: HttpsUrl | None = Field(alias="logo_uri#es-BO", title="Logo URI (Spanish (Bolivia))", default=None,
                                            placeholder="https://sub.example.com")
    logo_uri_es_cl: HttpsUrl | None = Field(alias="logo_uri#es-CL", title="Logo URI (Spanish (Chile))", default=None,
                                            placeholder="https://sub.example.com")
    logo_uri_es_co: HttpsUrl | None = Field(alias="logo_uri#es-CO", title="Logo URI (Spanish (Colombia))", default=None,
                                            placeholder="https://sub.example.com")
    logo_uri_es_cr: HttpsUrl | None = Field(alias="logo_uri#es-CR", title="Logo URI (Spanish (Costa Rica))",
                                            default=None, placeholder="https://sub.example.com")
    logo_uri_es_do: HttpsUrl | None = Field(alias="logo_uri#es-DO", title="Logo URI (Spanish (Dominican Republic))",
                                            default=None, placeholder="https://sub.example.com")
    logo_uri_es_ec: HttpsUrl | None = Field(alias="logo_uri#es-EC", title="Logo URI (Spanish (Ecuador))", default=None,
                                            placeholder="https://sub.example.com")
    logo_uri_es_es: HttpsUrl | None = Field(alias="logo_uri#es-ES", title="Logo URI (Spanish (Spain))", default=None,
                                            placeholder="https://sub.example.com")
    logo_uri_es_gt: HttpsUrl | None = Field(alias="logo_uri#es-GT", title="Logo URI (Spanish (Guatemala))",
                                            default=None, placeholder="https://sub.example.com")
    logo_uri_es_hn: HttpsUrl | None = Field(alias="logo_uri#es-HN", title="Logo URI (Spanish (Honduras))", default=None,
                                            placeholder="https://sub.example.com")
    logo_uri_es_mx: HttpsUrl | None = Field(alias="logo_uri#es-MX", title="Logo URI (Spanish (Mexico))", default=None,
                                            placeholder="https://sub.example.com")
    logo_uri_es_ni: HttpsUrl | None = Field(alias="logo_uri#es-NI", title="Logo URI (Spanish (Nicaragua))",
                                            default=None, placeholder="https://sub.example.com")
    logo_uri_es_pa: HttpsUrl | None = Field(alias="logo_uri#es-PA", title="Logo URI (Spanish (Panama))", default=None,
                                            placeholder="https://sub.example.com")
    logo_uri_es_pe: HttpsUrl | None = Field(alias="logo_uri#es-PE", title="Logo URI (Spanish (Peru))", default=None,
                                            placeholder="https://sub.example.com")
    logo_uri_es_pr: HttpsUrl | None = Field(alias="logo_uri#es-PR", title="Logo URI (Spanish (Puerto Rico))",
                                            default=None, placeholder="https://sub.example.com")
    logo_uri_es_py: HttpsUrl | None = Field(alias="logo_uri#es-PY", title="Logo URI (Spanish (Paraguay))", default=None,
                                            placeholder="https://sub.example.com")
    logo_uri_es_sv: HttpsUrl | None = Field(alias="logo_uri#es-SV", title="Logo URI (Spanish (El Salvador))",
                                            default=None, placeholder="https://sub.example.com")
    logo_uri_es_uy: HttpsUrl | None = Field(alias="logo_uri#es-UY", title="Logo URI (Spanish (Uruguay))", default=None,
                                            placeholder="https://sub.example.com")
    logo_uri_es_ve: HttpsUrl | None = Field(alias="logo_uri#es-VE", title="Logo URI (Spanish (Venezuela))",
                                            default=None, placeholder="https://sub.example.com")
    logo_uri_et_ee: HttpsUrl | None = Field(alias="logo_uri#et-EE", title="Logo URI (Estonian (Estonia))", default=None,
                                            placeholder="https://sub.example.com")
    logo_uri_eu_es: HttpsUrl | None = Field(alias="logo_uri#eu-ES", title="Logo URI (Basque (Spain))", default=None,
                                            placeholder="https://sub.example.com")
    logo_uri_fa_ir: HttpsUrl | None = Field(alias="logo_uri#fa-IR", title="Logo URI (Farsi (Iran))", default=None,
                                            placeholder="https://sub.example.com")
    logo_uri_fi_fi: HttpsUrl | None = Field(alias="logo_uri#fi-FI", title="Logo URI (Finnish (Finland))", default=None,
                                            placeholder="https://sub.example.com")
    logo_uri_fo_fo: HttpsUrl | None = Field(alias="logo_uri#fo-FO", title="Logo URI (Faroese (Faroe Islands))",
                                            default=None, placeholder="https://sub.example.com")
    logo_uri_fr_be: HttpsUrl | None = Field(alias="logo_uri#fr-BE", title="Logo URI (French (Belgium))", default=None,
                                            placeholder="https://sub.example.com")
    logo_uri_fr_ca: HttpsUrl | None = Field(alias="logo_uri#fr-CA", title="Logo URI (French (Canada))", default=None,
                                            placeholder="https://sub.example.com")
    logo_uri_fr_ch: HttpsUrl | None = Field(alias="logo_uri#fr-CH", title="Logo URI (French (Switzerland))",
                                            default=None, placeholder="https://sub.example.com")
    logo_uri_fr_fr: HttpsUrl | None = Field(alias="logo_uri#fr-FR", title="Logo URI (French (France))", default=None,
                                            placeholder="https://sub.example.com")
    logo_uri_fr_lu: HttpsUrl | None = Field(alias="logo_uri#fr-LU", title="Logo URI (French (Luxembourg))",
                                            default=None, placeholder="https://sub.example.com")
    logo_uri_fr_mc: HttpsUrl | None = Field(alias="logo_uri#fr-MC", title="Logo URI (French (Principality of Monaco))",
                                            default=None, placeholder="https://sub.example.com")
    logo_uri_gl_es: HttpsUrl | None = Field(alias="logo_uri#gl-ES", title="Logo URI (Galician (Spain))", default=None,
                                            placeholder="https://sub.example.com")
    logo_uri_gu_in: HttpsUrl | None = Field(alias="logo_uri#gu-IN", title="Logo URI (Gujarati (India))", default=None,
                                            placeholder="https://sub.example.com")
    logo_uri_he_il: HttpsUrl | None = Field(alias="logo_uri#he-IL", title="Logo URI (Hebrew (Israel))", default=None,
                                            placeholder="https://sub.example.com")
    logo_uri_hi_in: HttpsUrl | None = Field(alias="logo_uri#hi-IN", title="Logo URI (Hindi (India))", default=None,
                                            placeholder="https://sub.example.com")
    logo_uri_hr_ba: HttpsUrl | None = Field(alias="logo_uri#hr-BA",
                                            title="Logo URI (Croatian (Bosnia and Herzegovina))", default=None,
                                            placeholder="https://sub.example.com")
    logo_uri_hr_hr: HttpsUrl | None = Field(alias="logo_uri#hr-HR", title="Logo URI (Croatian (Croatia))", default=None,
                                            placeholder="https://sub.example.com")
    logo_uri_hu_hu: HttpsUrl | None = Field(alias="logo_uri#hu-HU", title="Logo URI (Hungarian (Hungary))",
                                            default=None, placeholder="https://sub.example.com")
    logo_uri_hy_am: HttpsUrl | None = Field(alias="logo_uri#hy-AM", title="Logo URI (Armenian (Armenia))", default=None,
                                            placeholder="https://sub.example.com")
    logo_uri_id_id: HttpsUrl | None = Field(alias="logo_uri#id-ID", title="Logo URI (Indonesian (Indonesia))",
                                            default=None, placeholder="https://sub.example.com")
    logo_uri_is_is: HttpsUrl | None = Field(alias="logo_uri#is-IS", title="Logo URI (Icelandic (Iceland))",
                                            default=None, placeholder="https://sub.example.com")
    logo_uri_it_ch: HttpsUrl | None = Field(alias="logo_uri#it-CH", title="Logo URI (Italian (Switzerland))",
                                            default=None, placeholder="https://sub.example.com")
    logo_uri_it_it: HttpsUrl | None = Field(alias="logo_uri#it-IT", title="Logo URI (Italian (Italy))", default=None,
                                            placeholder="https://sub.example.com")
    logo_uri_ja_jp: HttpsUrl | None = Field(alias="logo_uri#ja-JP", title="Logo URI (Japanese (Japan))", default=None,
                                            placeholder="https://sub.example.com")
    logo_uri_ka_ge: HttpsUrl | None = Field(alias="logo_uri#ka-GE", title="Logo URI (Georgian (Georgia))", default=None,
                                            placeholder="https://sub.example.com")
    logo_uri_kk_kz: HttpsUrl | None = Field(alias="logo_uri#kk-KZ", title="Logo URI (Kazakh (Kazakhstan))",
                                            default=None, placeholder="https://sub.example.com")
    logo_uri_kn_in: HttpsUrl | None = Field(alias="logo_uri#kn-IN", title="Logo URI (Kannada (India))", default=None,
                                            placeholder="https://sub.example.com")
    logo_uri_ko_kr: HttpsUrl | None = Field(alias="logo_uri#ko-KR", title="Logo URI (Korean (Korea))", default=None,
                                            placeholder="https://sub.example.com")
    logo_uri_kok_in: HttpsUrl | None = Field(alias="logo_uri#kok-IN", title="Logo URI (Konkani (India))", default=None,
                                             placeholder="https://sub.example.com")
    logo_uri_ky_kg: HttpsUrl | None = Field(alias="logo_uri#ky-KG", title="Logo URI (Kyrgyz (Kyrgyzstan))",
                                            default=None, placeholder="https://sub.example.com")
    logo_uri_lt_lt: HttpsUrl | None = Field(alias="logo_uri#lt-LT", title="Logo URI (Lithuanian (Lithuania))",
                                            default=None, placeholder="https://sub.example.com")
    logo_uri_lv_lv: HttpsUrl | None = Field(alias="logo_uri#lv-LV", title="Logo URI (Latvian (Latvia))", default=None,
                                            placeholder="https://sub.example.com")
    logo_uri_mi_nz: HttpsUrl | None = Field(alias="logo_uri#mi-NZ", title="Logo URI (Maori (New Zealand))",
                                            default=None, placeholder="https://sub.example.com")
    logo_uri_mk_mk: HttpsUrl | None = Field(alias="logo_uri#mk-MK",
                                            title="Logo URI (FYRO Macedonian (Former Yugoslav Republic of Macedonia))",
                                            default=None, placeholder="https://sub.example.com")
    logo_uri_mn_mn: HttpsUrl | None = Field(alias="logo_uri#mn-MN", title="Logo URI (Mongolian (Mongolia))",
                                            default=None, placeholder="https://sub.example.com")
    logo_uri_mr_in: HttpsUrl | None = Field(alias="logo_uri#mr-IN", title="Logo URI (Marathi (India))", default=None,
                                            placeholder="https://sub.example.com")
    logo_uri_ms_bn: HttpsUrl | None = Field(alias="logo_uri#ms-BN", title="Logo URI (Malay (Brunei Darussalam))",
                                            default=None, placeholder="https://sub.example.com")
    logo_uri_ms_my: HttpsUrl | None = Field(alias="logo_uri#ms-MY", title="Logo URI (Malay (Malaysia))", default=None,
                                            placeholder="https://sub.example.com")
    logo_uri_mt_mt: HttpsUrl | None = Field(alias="logo_uri#mt-MT", title="Logo URI (Maltese (Malta))", default=None,
                                            placeholder="https://sub.example.com")
    logo_uri_nb_no: HttpsUrl | None = Field(alias="logo_uri#nb-NO", title="Logo URI (Norwegian (Bokm?l) (Norway))",
                                            default=None, placeholder="https://sub.example.com")
    logo_uri_nl_be: HttpsUrl | None = Field(alias="logo_uri#nl-BE", title="Logo URI (Dutch (Belgium))", default=None,
                                            placeholder="https://sub.example.com")
    logo_uri_nl_nl: HttpsUrl | None = Field(alias="logo_uri#nl-NL", title="Logo URI (Dutch (Netherlands))",
                                            default=None, placeholder="https://sub.example.com")
    logo_uri_nn_no: HttpsUrl | None = Field(alias="logo_uri#nn-NO", title="Logo URI (Norwegian (Nynorsk) (Norway))",
                                            default=None, placeholder="https://sub.example.com")
    logo_uri_ns_za: HttpsUrl | None = Field(alias="logo_uri#ns-ZA", title="Logo URI (Northern Sotho (South Africa))",
                                            default=None, placeholder="https://sub.example.com")
    logo_uri_pa_in: HttpsUrl | None = Field(alias="logo_uri#pa-IN", title="Logo URI (Punjabi (India))", default=None,
                                            placeholder="https://sub.example.com")
    logo_uri_pl_pl: HttpsUrl | None = Field(alias="logo_uri#pl-PL", title="Logo URI (Polish (Poland))", default=None,
                                            placeholder="https://sub.example.com")
    logo_uri_ps_ar: HttpsUrl | None = Field(alias="logo_uri#ps-AR", title="Logo URI (Pashto (Afghanistan))",
                                            default=None, placeholder="https://sub.example.com")
    logo_uri_pt_br: HttpsUrl | None = Field(alias="logo_uri#pt-BR", title="Logo URI (Portuguese (Brazil))",
                                            default=None, placeholder="https://sub.example.com")
    logo_uri_pt_pt: HttpsUrl | None = Field(alias="logo_uri#pt-PT", title="Logo URI (Portuguese (Portugal))",
                                            default=None, placeholder="https://sub.example.com")
    logo_uri_qu_bo: HttpsUrl | None = Field(alias="logo_uri#qu-BO", title="Logo URI (Quechua (Bolivia))", default=None,
                                            placeholder="https://sub.example.com")
    logo_uri_qu_ec: HttpsUrl | None = Field(alias="logo_uri#qu-EC", title="Logo URI (Quechua (Ecuador))", default=None,
                                            placeholder="https://sub.example.com")
    logo_uri_qu_pe: HttpsUrl | None = Field(alias="logo_uri#qu-PE", title="Logo URI (Quechua (Peru))", default=None,
                                            placeholder="https://sub.example.com")
    logo_uri_ro_ro: HttpsUrl | None = Field(alias="logo_uri#ro-RO", title="Logo URI (Romanian (Romania))", default=None,
                                            placeholder="https://sub.example.com")
    logo_uri_ru_ru: HttpsUrl | None = Field(alias="logo_uri#ru-RU", title="Logo URI (Russian (Russia))", default=None,
                                            placeholder="https://sub.example.com")
    logo_uri_sa_in: HttpsUrl | None = Field(alias="logo_uri#sa-IN", title="Logo URI (Sanskrit (India))", default=None,
                                            placeholder="https://sub.example.com")
    logo_uri_se_fi: HttpsUrl | None = Field(alias="logo_uri#se-FI", title="Logo URI (Sami (Finland))", default=None,
                                            placeholder="https://sub.example.com")
    logo_uri_se_no: HttpsUrl | None = Field(alias="logo_uri#se-NO", title="Logo URI (Sami (Norway))", default=None,
                                            placeholder="https://sub.example.com")
    logo_uri_se_se: HttpsUrl | None = Field(alias="logo_uri#se-SE", title="Logo URI (Sami (Sweden))", default=None,
                                            placeholder="https://sub.example.com")
    logo_uri_sk_sk: HttpsUrl | None = Field(alias="logo_uri#sk-SK", title="Logo URI (Slovak (Slovakia))", default=None,
                                            placeholder="https://sub.example.com")
    logo_uri_sl_si: HttpsUrl | None = Field(alias="logo_uri#sl-SI", title="Logo URI (Slovenian (Slovenia))",
                                            default=None, placeholder="https://sub.example.com")
    logo_uri_sq_al: HttpsUrl | None = Field(alias="logo_uri#sq-AL", title="Logo URI (Albanian (Albania))", default=None,
                                            placeholder="https://sub.example.com")
    logo_uri_sr_ba: HttpsUrl | None = Field(alias="logo_uri#sr-BA",
                                            title="Logo URI (Serbian (Latin) (Bosnia and Herzegovina))", default=None,
                                            placeholder="https://sub.example.com")
    logo_uri_sr_cyrl_ba: HttpsUrl | None = Field(alias="logo_uri#sr-Cyrl-BA",
                                                 title="Logo URI (Serbian (Cyrillic) (Bosnia and Herzegovina))",
                                                 default=None, placeholder="https://sub.example.com")
    logo_uri_sr_sp: HttpsUrl | None = Field(alias="logo_uri#sr-SP",
                                            title="Logo URI (Serbian (Latin) (Serbia and Montenegro))", default=None,
                                            placeholder="https://sub.example.com")
    logo_uri_sr_cyrl_sp: HttpsUrl | None = Field(alias="logo_uri#sr-Cyrl-SP",
                                                 title="Logo URI (Serbian (Cyrillic) (Serbia and Montenegro))",
                                                 default=None, placeholder="https://sub.example.com")
    logo_uri_sv_fi: HttpsUrl | None = Field(alias="logo_uri#sv-FI", title="Logo URI (Swedish (Finland))", default=None,
                                            placeholder="https://sub.example.com")
    logo_uri_sv_se: HttpsUrl | None = Field(alias="logo_uri#sv-SE", title="Logo URI (Swedish (Sweden))", default=None,
                                            placeholder="https://sub.example.com")
    logo_uri_sw_ke: HttpsUrl | None = Field(alias="logo_uri#sw-KE", title="Logo URI (Swahili (Kenya))", default=None,
                                            placeholder="https://sub.example.com")
    logo_uri_syr_sy: HttpsUrl | None = Field(alias="logo_uri#syr-SY", title="Logo URI (Syriac (Syria))", default=None,
                                             placeholder="https://sub.example.com")
    logo_uri_ta_in: HttpsUrl | None = Field(alias="logo_uri#ta-IN", title="Logo URI (Tamil (India))", default=None,
                                            placeholder="https://sub.example.com")
    logo_uri_te_in: HttpsUrl | None = Field(alias="logo_uri#te-IN", title="Logo URI (Telugu (India))", default=None,
                                            placeholder="https://sub.example.com")
    logo_uri_th_th: HttpsUrl | None = Field(alias="logo_uri#th-TH", title="Logo URI (Thai (Thailand))", default=None,
                                            placeholder="https://sub.example.com")
    logo_uri_tl_ph: HttpsUrl | None = Field(alias="logo_uri#tl-PH", title="Logo URI (Tagalog (Philippines))",
                                            default=None, placeholder="https://sub.example.com")
    logo_uri_tn_za: HttpsUrl | None = Field(alias="logo_uri#tn-ZA", title="Logo URI (Tswana (South Africa))",
                                            default=None, placeholder="https://sub.example.com")
    logo_uri_tr_tr: HttpsUrl | None = Field(alias="logo_uri#tr-TR", title="Logo URI (Turkish (Turkey))", default=None,
                                            placeholder="https://sub.example.com")
    logo_uri_tt_ru: HttpsUrl | None = Field(alias="logo_uri#tt-RU", title="Logo URI (Tatar (Russia))", default=None,
                                            placeholder="https://sub.example.com")
    logo_uri_uk_ua: HttpsUrl | None = Field(alias="logo_uri#uk-UA", title="Logo URI (Ukrainian (Ukraine))",
                                            default=None, placeholder="https://sub.example.com")
    logo_uri_ur_pk: HttpsUrl | None = Field(alias="logo_uri#ur-PK",
                                            title="Logo URI (Urdu (Islamic Republic of Pakistan))", default=None,
                                            placeholder="https://sub.example.com")
    logo_uri_uz_uz: HttpsUrl | None = Field(alias="logo_uri#uz-UZ", title="Logo URI (Uzbek (Latin) (Uzbekistan))",
                                            default=None, placeholder="https://sub.example.com")
    logo_uri_uz_cyrl_uz: HttpsUrl | None = Field(alias="logo_uri#uz-Cyrl-UZ",
                                                 title="Logo URI (Uzbek (Cyrillic) (Uzbekistan))", default=None,
                                                 placeholder="https://sub.example.com")
    logo_uri_vi_vn: HttpsUrl | None = Field(alias="logo_uri#vi-VN", title="Logo URI (Vietnamese (Viet Nam))",
                                            default=None, placeholder="https://sub.example.com")
    logo_uri_xh_za: HttpsUrl | None = Field(alias="logo_uri#xh-ZA", title="Logo URI (Xhosa (South Africa))",
                                            default=None, placeholder="https://sub.example.com")
    logo_uri_zh_cn: HttpsUrl | None = Field(alias="logo_uri#zh-CN", title="Logo URI (Chinese (S))", default=None,
                                            placeholder="https://sub.example.com")
    logo_uri_zh_hk: HttpsUrl | None = Field(alias="logo_uri#zh-HK", title="Logo URI (Chinese (Hong Kong))",
                                            default=None, placeholder="https://sub.example.com")
    logo_uri_zh_mo: HttpsUrl | None = Field(alias="logo_uri#zh-MO", title="Logo URI (Chinese (Macau))", default=None,
                                            placeholder="https://sub.example.com")
    logo_uri_zh_sg: HttpsUrl | None = Field(alias="logo_uri#zh-SG", title="Logo URI (Chinese (Singapore))",
                                            default=None, placeholder="https://sub.example.com")
    logo_uri_zh_tw: HttpsUrl | None = Field(alias="logo_uri#zh-TW", title="Logo URI (Chinese (T))", default=None,
                                            placeholder="https://sub.example.com")
    logo_uri_zu_za: HttpsUrl | None = Field(alias="logo_uri#zu-ZA", title="Logo URI (Zulu (South Africa))",
                                            default=None, placeholder="https://sub.example.com")


class ClientURILangs(BaseModel):
    client_uri_af_za: HttpsUrl | None = Field(alias="client_uri#af-ZA", title="Client URI (Afrikaans (South Africa))",
                                              default=None, placeholder="https://sub.example.com")
    client_uri_ar_ae: HttpsUrl | None = Field(alias="client_uri#ar-AE", title="Client URI (Arabic (U.A.E.))",
                                              default=None, placeholder="https://sub.example.com")
    client_uri_ar_bh: HttpsUrl | None = Field(alias="client_uri#ar-BH", title="Client URI (Arabic (Bahrain))",
                                              default=None, placeholder="https://sub.example.com")
    client_uri_ar_dz: HttpsUrl | None = Field(alias="client_uri#ar-DZ", title="Client URI (Arabic (Algeria))",
                                              default=None, placeholder="https://sub.example.com")
    client_uri_ar_eg: HttpsUrl | None = Field(alias="client_uri#ar-EG", title="Client URI (Arabic (Egypt))",
                                              default=None, placeholder="https://sub.example.com")
    client_uri_ar_iq: HttpsUrl | None = Field(alias="client_uri#ar-IQ", title="Client URI (Arabic (Iraq))",
                                              default=None, placeholder="https://sub.example.com")
    client_uri_ar_jo: HttpsUrl | None = Field(alias="client_uri#ar-JO", title="Client URI (Arabic (Jordan))",
                                              default=None, placeholder="https://sub.example.com")
    client_uri_ar_kw: HttpsUrl | None = Field(alias="client_uri#ar-KW", title="Client URI (Arabic (Kuwait))",
                                              default=None, placeholder="https://sub.example.com")
    client_uri_ar_lb: HttpsUrl | None = Field(alias="client_uri#ar-LB", title="Client URI (Arabic (Lebanon))",
                                              default=None, placeholder="https://sub.example.com")
    client_uri_ar_ly: HttpsUrl | None = Field(alias="client_uri#ar-LY", title="Client URI (Arabic (Libya))",
                                              default=None, placeholder="https://sub.example.com")
    client_uri_ar_ma: HttpsUrl | None = Field(alias="client_uri#ar-MA", title="Client URI (Arabic (Morocco))",
                                              default=None, placeholder="https://sub.example.com")
    client_uri_ar_om: HttpsUrl | None = Field(alias="client_uri#ar-OM", title="Client URI (Arabic (Oman))",
                                              default=None, placeholder="https://sub.example.com")
    client_uri_ar_qa: HttpsUrl | None = Field(alias="client_uri#ar-QA", title="Client URI (Arabic (Qatar))",
                                              default=None, placeholder="https://sub.example.com")
    client_uri_ar_sa: HttpsUrl | None = Field(alias="client_uri#ar-SA", title="Client URI (Arabic (Saudi Arabia))",
                                              default=None, placeholder="https://sub.example.com")
    client_uri_ar_sy: HttpsUrl | None = Field(alias="client_uri#ar-SY", title="Client URI (Arabic (Syria))",
                                              default=None, placeholder="https://sub.example.com")
    client_uri_ar_tn: HttpsUrl | None = Field(alias="client_uri#ar-TN", title="Client URI (Arabic (Tunisia))",
                                              default=None, placeholder="https://sub.example.com")
    client_uri_ar_ye: HttpsUrl | None = Field(alias="client_uri#ar-YE", title="Client URI (Arabic (Yemen))",
                                              default=None, placeholder="https://sub.example.com")
    client_uri_az_az: HttpsUrl | None = Field(alias="client_uri#az-AZ", title="Client URI (Azeri (Latin) (Azerbaijan))",
                                              default=None, placeholder="https://sub.example.com")
    client_uri_az_cyrl_az: HttpsUrl | None = Field(alias="client_uri#az-Cyrl-AZ",
                                                   title="Client URI (Azeri (Cyrillic) (Azerbaijan))", default=None,
                                                   placeholder="https://sub.example.com")
    client_uri_be_by: HttpsUrl | None = Field(alias="client_uri#be-BY", title="Client URI (Belarusian (Belarus))",
                                              default=None, placeholder="https://sub.example.com")
    client_uri_bg_bg: HttpsUrl | None = Field(alias="client_uri#bg-BG", title="Client URI (Bulgarian (Bulgaria))",
                                              default=None, placeholder="https://sub.example.com")
    client_uri_bs_ba: HttpsUrl | None = Field(alias="client_uri#bs-BA",
                                              title="Client URI (Bosnian (Bosnia and Herzegovina))", default=None,
                                              placeholder="https://sub.example.com")
    client_uri_ca_es: HttpsUrl | None = Field(alias="client_uri#ca-ES", title="Client URI (Catalan (Spain))",
                                              default=None, placeholder="https://sub.example.com")
    client_uri_cs_cz: HttpsUrl | None = Field(alias="client_uri#cs-CZ", title="Client URI (Czech (Czech Republic))",
                                              default=None, placeholder="https://sub.example.com")
    client_uri_cy_gb: HttpsUrl | None = Field(alias="client_uri#cy-GB", title="Client URI (Welsh (United Kingdom))",
                                              default=None, placeholder="https://sub.example.com")
    client_uri_da_dk: HttpsUrl | None = Field(alias="client_uri#da-DK", title="Client URI (Danish (Denmark))",
                                              default=None, placeholder="https://sub.example.com")
    client_uri_de_at: HttpsUrl | None = Field(alias="client_uri#de-AT", title="Client URI (German (Austria))",
                                              default=None, placeholder="https://sub.example.com")
    client_uri_de_ch: HttpsUrl | None = Field(alias="client_uri#de-CH", title="Client URI (German (Switzerland))",
                                              default=None, placeholder="https://sub.example.com")
    client_uri_de_de: HttpsUrl | None = Field(alias="client_uri#de-DE", title="Client URI (German (Germany))",
                                              default=None, placeholder="https://sub.example.com")
    client_uri_de_li: HttpsUrl | None = Field(alias="client_uri#de-LI", title="Client URI (German (Liechtenstein))",
                                              default=None, placeholder="https://sub.example.com")
    client_uri_de_lu: HttpsUrl | None = Field(alias="client_uri#de-LU", title="Client URI (German (Luxembourg))",
                                              default=None, placeholder="https://sub.example.com")
    client_uri_dv_mv: HttpsUrl | None = Field(alias="client_uri#dv-MV", title="Client URI (Divehi (Maldives))",
                                              default=None, placeholder="https://sub.example.com")
    client_uri_el_gr: HttpsUrl | None = Field(alias="client_uri#el-GR", title="Client URI (Greek (Greece))",
                                              default=None, placeholder="https://sub.example.com")
    client_uri_en_au: HttpsUrl | None = Field(alias="client_uri#en-AU", title="Client URI (English (Australia))",
                                              default=None, placeholder="https://sub.example.com")
    client_uri_en_bz: HttpsUrl | None = Field(alias="client_uri#en-BZ", title="Client URI (English (Belize))",
                                              default=None, placeholder="https://sub.example.com")
    client_uri_en_ca: HttpsUrl | None = Field(alias="client_uri#en-CA", title="Client URI (English (Canada))",
                                              default=None, placeholder="https://sub.example.com")
    client_uri_en_cb: HttpsUrl | None = Field(alias="client_uri#en-CB", title="Client URI (English (Caribbean))",
                                              default=None, placeholder="https://sub.example.com")
    client_uri_en_gb: HttpsUrl | None = Field(alias="client_uri#en-GB", title="Client URI (English (United Kingdom))",
                                              default=None, placeholder="https://sub.example.com")
    client_uri_en_ie: HttpsUrl | None = Field(alias="client_uri#en-IE", title="Client URI (English (Ireland))",
                                              default=None, placeholder="https://sub.example.com")
    client_uri_en_jm: HttpsUrl | None = Field(alias="client_uri#en-JM", title="Client URI (English (Jamaica))",
                                              default=None, placeholder="https://sub.example.com")
    client_uri_en_nz: HttpsUrl | None = Field(alias="client_uri#en-NZ", title="Client URI (English (New Zealand))",
                                              default=None, placeholder="https://sub.example.com")
    client_uri_en_ph: HttpsUrl | None = Field(alias="client_uri#en-PH",
                                              title="Client URI (English (Republic of the Philippines))", default=None,
                                              placeholder="https://sub.example.com")
    client_uri_en_tt: HttpsUrl | None = Field(alias="client_uri#en-TT",
                                              title="Client URI (English (Trinidad and Tobago))", default=None,
                                              placeholder="https://sub.example.com")
    client_uri_en_us: HttpsUrl | None = Field(alias="client_uri#en-US", title="Client URI (English (United States))",
                                              default=None, placeholder="https://sub.example.com")
    client_uri_en_za: HttpsUrl | None = Field(alias="client_uri#en-ZA", title="Client URI (English (South Africa))",
                                              default=None, placeholder="https://sub.example.com")
    client_uri_en_zw: HttpsUrl | None = Field(alias="client_uri#en-ZW", title="Client URI (English (Zimbabwe))",
                                              default=None, placeholder="https://sub.example.com")
    client_uri_es_ar: HttpsUrl | None = Field(alias="client_uri#es-AR", title="Client URI (Spanish (Argentina))",
                                              default=None, placeholder="https://sub.example.com")
    client_uri_es_bo: HttpsUrl | None = Field(alias="client_uri#es-BO", title="Client URI (Spanish (Bolivia))",
                                              default=None, placeholder="https://sub.example.com")
    client_uri_es_cl: HttpsUrl | None = Field(alias="client_uri#es-CL", title="Client URI (Spanish (Chile))",
                                              default=None, placeholder="https://sub.example.com")
    client_uri_es_co: HttpsUrl | None = Field(alias="client_uri#es-CO", title="Client URI (Spanish (Colombia))",
                                              default=None, placeholder="https://sub.example.com")
    client_uri_es_cr: HttpsUrl | None = Field(alias="client_uri#es-CR", title="Client URI (Spanish (Costa Rica))",
                                              default=None, placeholder="https://sub.example.com")
    client_uri_es_do: HttpsUrl | None = Field(alias="client_uri#es-DO",
                                              title="Client URI (Spanish (Dominican Republic))", default=None,
                                              placeholder="https://sub.example.com")
    client_uri_es_ec: HttpsUrl | None = Field(alias="client_uri#es-EC", title="Client URI (Spanish (Ecuador))",
                                              default=None, placeholder="https://sub.example.com")
    client_uri_es_es: HttpsUrl | None = Field(alias="client_uri#es-ES", title="Client URI (Spanish (Spain))",
                                              default=None, placeholder="https://sub.example.com")
    client_uri_es_gt: HttpsUrl | None = Field(alias="client_uri#es-GT", title="Client URI (Spanish (Guatemala))",
                                              default=None, placeholder="https://sub.example.com")
    client_uri_es_hn: HttpsUrl | None = Field(alias="client_uri#es-HN", title="Client URI (Spanish (Honduras))",
                                              default=None, placeholder="https://sub.example.com")
    client_uri_es_mx: HttpsUrl | None = Field(alias="client_uri#es-MX", title="Client URI (Spanish (Mexico))",
                                              default=None, placeholder="https://sub.example.com")
    client_uri_es_ni: HttpsUrl | None = Field(alias="client_uri#es-NI", title="Client URI (Spanish (Nicaragua))",
                                              default=None, placeholder="https://sub.example.com")
    client_uri_es_pa: HttpsUrl | None = Field(alias="client_uri#es-PA", title="Client URI (Spanish (Panama))",
                                              default=None, placeholder="https://sub.example.com")
    client_uri_es_pe: HttpsUrl | None = Field(alias="client_uri#es-PE", title="Client URI (Spanish (Peru))",
                                              default=None, placeholder="https://sub.example.com")
    client_uri_es_pr: HttpsUrl | None = Field(alias="client_uri#es-PR", title="Client URI (Spanish (Puerto Rico))",
                                              default=None, placeholder="https://sub.example.com")
    client_uri_es_py: HttpsUrl | None = Field(alias="client_uri#es-PY", title="Client URI (Spanish (Paraguay))",
                                              default=None, placeholder="https://sub.example.com")
    client_uri_es_sv: HttpsUrl | None = Field(alias="client_uri#es-SV", title="Client URI (Spanish (El Salvador))",
                                              default=None, placeholder="https://sub.example.com")
    client_uri_es_uy: HttpsUrl | None = Field(alias="client_uri#es-UY", title="Client URI (Spanish (Uruguay))",
                                              default=None, placeholder="https://sub.example.com")
    client_uri_es_ve: HttpsUrl | None = Field(alias="client_uri#es-VE", title="Client URI (Spanish (Venezuela))",
                                              default=None, placeholder="https://sub.example.com")
    client_uri_et_ee: HttpsUrl | None = Field(alias="client_uri#et-EE", title="Client URI (Estonian (Estonia))",
                                              default=None, placeholder="https://sub.example.com")
    client_uri_eu_es: HttpsUrl | None = Field(alias="client_uri#eu-ES", title="Client URI (Basque (Spain))",
                                              default=None, placeholder="https://sub.example.com")
    client_uri_fa_ir: HttpsUrl | None = Field(alias="client_uri#fa-IR", title="Client URI (Farsi (Iran))", default=None,
                                              placeholder="https://sub.example.com")
    client_uri_fi_fi: HttpsUrl | None = Field(alias="client_uri#fi-FI", title="Client URI (Finnish (Finland))",
                                              default=None, placeholder="https://sub.example.com")
    client_uri_fo_fo: HttpsUrl | None = Field(alias="client_uri#fo-FO", title="Client URI (Faroese (Faroe Islands))",
                                              default=None, placeholder="https://sub.example.com")
    client_uri_fr_be: HttpsUrl | None = Field(alias="client_uri#fr-BE", title="Client URI (French (Belgium))",
                                              default=None, placeholder="https://sub.example.com")
    client_uri_fr_ca: HttpsUrl | None = Field(alias="client_uri#fr-CA", title="Client URI (French (Canada))",
                                              default=None, placeholder="https://sub.example.com")
    client_uri_fr_ch: HttpsUrl | None = Field(alias="client_uri#fr-CH", title="Client URI (French (Switzerland))",
                                              default=None, placeholder="https://sub.example.com")
    client_uri_fr_fr: HttpsUrl | None = Field(alias="client_uri#fr-FR", title="Client URI (French (France))",
                                              default=None, placeholder="https://sub.example.com")
    client_uri_fr_lu: HttpsUrl | None = Field(alias="client_uri#fr-LU", title="Client URI (French (Luxembourg))",
                                              default=None, placeholder="https://sub.example.com")
    client_uri_fr_mc: HttpsUrl | None = Field(alias="client_uri#fr-MC",
                                              title="Client URI (French (Principality of Monaco))", default=None,
                                              placeholder="https://sub.example.com")
    client_uri_gl_es: HttpsUrl | None = Field(alias="client_uri#gl-ES", title="Client URI (Galician (Spain))",
                                              default=None, placeholder="https://sub.example.com")
    client_uri_gu_in: HttpsUrl | None = Field(alias="client_uri#gu-IN", title="Client URI (Gujarati (India))",
                                              default=None, placeholder="https://sub.example.com")
    client_uri_he_il: HttpsUrl | None = Field(alias="client_uri#he-IL", title="Client URI (Hebrew (Israel))",
                                              default=None, placeholder="https://sub.example.com")
    client_uri_hi_in: HttpsUrl | None = Field(alias="client_uri#hi-IN", title="Client URI (Hindi (India))",
                                              default=None, placeholder="https://sub.example.com")
    client_uri_hr_ba: HttpsUrl | None = Field(alias="client_uri#hr-BA",
                                              title="Client URI (Croatian (Bosnia and Herzegovina))", default=None,
                                              placeholder="https://sub.example.com")
    client_uri_hr_hr: HttpsUrl | None = Field(alias="client_uri#hr-HR", title="Client URI (Croatian (Croatia))",
                                              default=None, placeholder="https://sub.example.com")
    client_uri_hu_hu: HttpsUrl | None = Field(alias="client_uri#hu-HU", title="Client URI (Hungarian (Hungary))",
                                              default=None, placeholder="https://sub.example.com")
    client_uri_hy_am: HttpsUrl | None = Field(alias="client_uri#hy-AM", title="Client URI (Armenian (Armenia))",
                                              default=None, placeholder="https://sub.example.com")
    client_uri_id_id: HttpsUrl | None = Field(alias="client_uri#id-ID", title="Client URI (Indonesian (Indonesia))",
                                              default=None, placeholder="https://sub.example.com")
    client_uri_is_is: HttpsUrl | None = Field(alias="client_uri#is-IS", title="Client URI (Icelandic (Iceland))",
                                              default=None, placeholder="https://sub.example.com")
    client_uri_it_ch: HttpsUrl | None = Field(alias="client_uri#it-CH", title="Client URI (Italian (Switzerland))",
                                              default=None, placeholder="https://sub.example.com")
    client_uri_it_it: HttpsUrl | None = Field(alias="client_uri#it-IT", title="Client URI (Italian (Italy))",
                                              default=None, placeholder="https://sub.example.com")
    client_uri_ja_jp: HttpsUrl | None = Field(alias="client_uri#ja-JP", title="Client URI (Japanese (Japan))",
                                              default=None, placeholder="https://sub.example.com")
    client_uri_ka_ge: HttpsUrl | None = Field(alias="client_uri#ka-GE", title="Client URI (Georgian (Georgia))",
                                              default=None, placeholder="https://sub.example.com")
    client_uri_kk_kz: HttpsUrl | None = Field(alias="client_uri#kk-KZ", title="Client URI (Kazakh (Kazakhstan))",
                                              default=None, placeholder="https://sub.example.com")
    client_uri_kn_in: HttpsUrl | None = Field(alias="client_uri#kn-IN", title="Client URI (Kannada (India))",
                                              default=None, placeholder="https://sub.example.com")
    client_uri_ko_kr: HttpsUrl | None = Field(alias="client_uri#ko-KR", title="Client URI (Korean (Korea))",
                                              default=None, placeholder="https://sub.example.com")
    client_uri_kok_in: HttpsUrl | None = Field(alias="client_uri#kok-IN", title="Client URI (Konkani (India))",
                                               default=None, placeholder="https://sub.example.com")
    client_uri_ky_kg: HttpsUrl | None = Field(alias="client_uri#ky-KG", title="Client URI (Kyrgyz (Kyrgyzstan))",
                                              default=None, placeholder="https://sub.example.com")
    client_uri_lt_lt: HttpsUrl | None = Field(alias="client_uri#lt-LT", title="Client URI (Lithuanian (Lithuania))",
                                              default=None, placeholder="https://sub.example.com")
    client_uri_lv_lv: HttpsUrl | None = Field(alias="client_uri#lv-LV", title="Client URI (Latvian (Latvia))",
                                              default=None, placeholder="https://sub.example.com")
    client_uri_mi_nz: HttpsUrl | None = Field(alias="client_uri#mi-NZ", title="Client URI (Maori (New Zealand))",
                                              default=None, placeholder="https://sub.example.com")
    client_uri_mk_mk: HttpsUrl | None = Field(alias="client_uri#mk-MK",
                                              title="Client URI (FYRO Macedonian (Former Yugoslav Republic of Macedonia))",
                                              default=None, placeholder="https://sub.example.com")
    client_uri_mn_mn: HttpsUrl | None = Field(alias="client_uri#mn-MN", title="Client URI (Mongolian (Mongolia))",
                                              default=None, placeholder="https://sub.example.com")
    client_uri_mr_in: HttpsUrl | None = Field(alias="client_uri#mr-IN", title="Client URI (Marathi (India))",
                                              default=None, placeholder="https://sub.example.com")
    client_uri_ms_bn: HttpsUrl | None = Field(alias="client_uri#ms-BN", title="Client URI (Malay (Brunei Darussalam))",
                                              default=None, placeholder="https://sub.example.com")
    client_uri_ms_my: HttpsUrl | None = Field(alias="client_uri#ms-MY", title="Client URI (Malay (Malaysia))",
                                              default=None, placeholder="https://sub.example.com")
    client_uri_mt_mt: HttpsUrl | None = Field(alias="client_uri#mt-MT", title="Client URI (Maltese (Malta))",
                                              default=None, placeholder="https://sub.example.com")
    client_uri_nb_no: HttpsUrl | None = Field(alias="client_uri#nb-NO",
                                              title="Client URI (Norwegian (Bokm?l) (Norway))", default=None,
                                              placeholder="https://sub.example.com")
    client_uri_nl_be: HttpsUrl | None = Field(alias="client_uri#nl-BE", title="Client URI (Dutch (Belgium))",
                                              default=None, placeholder="https://sub.example.com")
    client_uri_nl_nl: HttpsUrl | None = Field(alias="client_uri#nl-NL", title="Client URI (Dutch (Netherlands))",
                                              default=None, placeholder="https://sub.example.com")
    client_uri_nn_no: HttpsUrl | None = Field(alias="client_uri#nn-NO",
                                              title="Client URI (Norwegian (Nynorsk) (Norway))", default=None,
                                              placeholder="https://sub.example.com")
    client_uri_ns_za: HttpsUrl | None = Field(alias="client_uri#ns-ZA",
                                              title="Client URI (Northern Sotho (South Africa))", default=None,
                                              placeholder="https://sub.example.com")
    client_uri_pa_in: HttpsUrl | None = Field(alias="client_uri#pa-IN", title="Client URI (Punjabi (India))",
                                              default=None, placeholder="https://sub.example.com")
    client_uri_pl_pl: HttpsUrl | None = Field(alias="client_uri#pl-PL", title="Client URI (Polish (Poland))",
                                              default=None, placeholder="https://sub.example.com")
    client_uri_ps_ar: HttpsUrl | None = Field(alias="client_uri#ps-AR", title="Client URI (Pashto (Afghanistan))",
                                              default=None, placeholder="https://sub.example.com")
    client_uri_pt_br: HttpsUrl | None = Field(alias="client_uri#pt-BR", title="Client URI (Portuguese (Brazil))",
                                              default=None, placeholder="https://sub.example.com")
    client_uri_pt_pt: HttpsUrl | None = Field(alias="client_uri#pt-PT", title="Client URI (Portuguese (Portugal))",
                                              default=None, placeholder="https://sub.example.com")
    client_uri_qu_bo: HttpsUrl | None = Field(alias="client_uri#qu-BO", title="Client URI (Quechua (Bolivia))",
                                              default=None, placeholder="https://sub.example.com")
    client_uri_qu_ec: HttpsUrl | None = Field(alias="client_uri#qu-EC", title="Client URI (Quechua (Ecuador))",
                                              default=None, placeholder="https://sub.example.com")
    client_uri_qu_pe: HttpsUrl | None = Field(alias="client_uri#qu-PE", title="Client URI (Quechua (Peru))",
                                              default=None, placeholder="https://sub.example.com")
    client_uri_ro_ro: HttpsUrl | None = Field(alias="client_uri#ro-RO", title="Client URI (Romanian (Romania))",
                                              default=None, placeholder="https://sub.example.com")
    client_uri_ru_ru: HttpsUrl | None = Field(alias="client_uri#ru-RU", title="Client URI (Russian (Russia))",
                                              default=None, placeholder="https://sub.example.com")
    client_uri_sa_in: HttpsUrl | None = Field(alias="client_uri#sa-IN", title="Client URI (Sanskrit (India))",
                                              default=None, placeholder="https://sub.example.com")
    client_uri_se_fi: HttpsUrl | None = Field(alias="client_uri#se-FI", title="Client URI (Sami (Finland))",
                                              default=None, placeholder="https://sub.example.com")
    client_uri_se_no: HttpsUrl | None = Field(alias="client_uri#se-NO", title="Client URI (Sami (Norway))",
                                              default=None, placeholder="https://sub.example.com")
    client_uri_se_se: HttpsUrl | None = Field(alias="client_uri#se-SE", title="Client URI (Sami (Sweden))",
                                              default=None, placeholder="https://sub.example.com")
    client_uri_sk_sk: HttpsUrl | None = Field(alias="client_uri#sk-SK", title="Client URI (Slovak (Slovakia))",
                                              default=None, placeholder="https://sub.example.com")
    client_uri_sl_si: HttpsUrl | None = Field(alias="client_uri#sl-SI", title="Client URI (Slovenian (Slovenia))",
                                              default=None, placeholder="https://sub.example.com")
    client_uri_sq_al: HttpsUrl | None = Field(alias="client_uri#sq-AL", title="Client URI (Albanian (Albania))",
                                              default=None, placeholder="https://sub.example.com")
    client_uri_sr_ba: HttpsUrl | None = Field(alias="client_uri#sr-BA",
                                              title="Client URI (Serbian (Latin) (Bosnia and Herzegovina))",
                                              default=None, placeholder="https://sub.example.com")
    client_uri_sr_cyrl_ba: HttpsUrl | None = Field(alias="client_uri#sr-Cyrl-BA",
                                                   title="Client URI (Serbian (Cyrillic) (Bosnia and Herzegovina))",
                                                   default=None, placeholder="https://sub.example.com")
    client_uri_sr_sp: HttpsUrl | None = Field(alias="client_uri#sr-SP",
                                              title="Client URI (Serbian (Latin) (Serbia and Montenegro))",
                                              default=None, placeholder="https://sub.example.com")
    client_uri_sr_cyrl_sp: HttpsUrl | None = Field(alias="client_uri#sr-Cyrl-SP",
                                                   title="Client URI (Serbian (Cyrillic) (Serbia and Montenegro))",
                                                   default=None, placeholder="https://sub.example.com")
    client_uri_sv_fi: HttpsUrl | None = Field(alias="client_uri#sv-FI", title="Client URI (Swedish (Finland))",
                                              default=None, placeholder="https://sub.example.com")
    client_uri_sv_se: HttpsUrl | None = Field(alias="client_uri#sv-SE", title="Client URI (Swedish (Sweden))",
                                              default=None, placeholder="https://sub.example.com")
    client_uri_sw_ke: HttpsUrl | None = Field(alias="client_uri#sw-KE", title="Client URI (Swahili (Kenya))",
                                              default=None, placeholder="https://sub.example.com")
    client_uri_syr_sy: HttpsUrl | None = Field(alias="client_uri#syr-SY", title="Client URI (Syriac (Syria))",
                                               default=None, placeholder="https://sub.example.com")
    client_uri_ta_in: HttpsUrl | None = Field(alias="client_uri#ta-IN", title="Client URI (Tamil (India))",
                                              default=None, placeholder="https://sub.example.com")
    client_uri_te_in: HttpsUrl | None = Field(alias="client_uri#te-IN", title="Client URI (Telugu (India))",
                                              default=None, placeholder="https://sub.example.com")
    client_uri_th_th: HttpsUrl | None = Field(alias="client_uri#th-TH", title="Client URI (Thai (Thailand))",
                                              default=None, placeholder="https://sub.example.com")
    client_uri_tl_ph: HttpsUrl | None = Field(alias="client_uri#tl-PH", title="Client URI (Tagalog (Philippines))",
                                              default=None, placeholder="https://sub.example.com")
    client_uri_tn_za: HttpsUrl | None = Field(alias="client_uri#tn-ZA", title="Client URI (Tswana (South Africa))",
                                              default=None, placeholder="https://sub.example.com")
    client_uri_tr_tr: HttpsUrl | None = Field(alias="client_uri#tr-TR", title="Client URI (Turkish (Turkey))",
                                              default=None, placeholder="https://sub.example.com")
    client_uri_tt_ru: HttpsUrl | None = Field(alias="client_uri#tt-RU", title="Client URI (Tatar (Russia))",
                                              default=None, placeholder="https://sub.example.com")
    client_uri_uk_ua: HttpsUrl | None = Field(alias="client_uri#uk-UA", title="Client URI (Ukrainian (Ukraine))",
                                              default=None, placeholder="https://sub.example.com")
    client_uri_ur_pk: HttpsUrl | None = Field(alias="client_uri#ur-PK",
                                              title="Client URI (Urdu (Islamic Republic of Pakistan))", default=None,
                                              placeholder="https://sub.example.com")
    client_uri_uz_uz: HttpsUrl | None = Field(alias="client_uri#uz-UZ", title="Client URI (Uzbek (Latin) (Uzbekistan))",
                                              default=None, placeholder="https://sub.example.com")
    client_uri_uz_cyrl_uz: HttpsUrl | None = Field(alias="client_uri#uz-Cyrl-UZ",
                                                   title="Client URI (Uzbek (Cyrillic) (Uzbekistan))", default=None,
                                                   placeholder="https://sub.example.com")
    client_uri_vi_vn: HttpsUrl | None = Field(alias="client_uri#vi-VN", title="Client URI (Vietnamese (Viet Nam))",
                                              default=None, placeholder="https://sub.example.com")
    client_uri_xh_za: HttpsUrl | None = Field(alias="client_uri#xh-ZA", title="Client URI (Xhosa (South Africa))",
                                              default=None, placeholder="https://sub.example.com")
    client_uri_zh_cn: HttpsUrl | None = Field(alias="client_uri#zh-CN", title="Client URI (Chinese (S))", default=None,
                                              placeholder="https://sub.example.com")
    client_uri_zh_hk: HttpsUrl | None = Field(alias="client_uri#zh-HK", title="Client URI (Chinese (Hong Kong))",
                                              default=None, placeholder="https://sub.example.com")
    client_uri_zh_mo: HttpsUrl | None = Field(alias="client_uri#zh-MO", title="Client URI (Chinese (Macau))",
                                              default=None, placeholder="https://sub.example.com")
    client_uri_zh_sg: HttpsUrl | None = Field(alias="client_uri#zh-SG", title="Client URI (Chinese (Singapore))",
                                              default=None, placeholder="https://sub.example.com")
    client_uri_zh_tw: HttpsUrl | None = Field(alias="client_uri#zh-TW", title="Client URI (Chinese (T))", default=None,
                                              placeholder="https://sub.example.com")
    client_uri_zu_za: HttpsUrl | None = Field(alias="client_uri#zu-ZA", title="Client URI (Zulu (South Africa))",
                                              default=None, placeholder="https://sub.example.com")


class ClientRegistrationRequest(ClientNameLangs, TOSURILangs, PolicyURILangs, LogoURILangs, ClientURILangs):
    model_config = ConfigDict(
            json_schema_extra={
                "examples": [
                    {
                        "redirect_uris": [
                            "https://client.example.org/callback",
                            "https://client.example.org/callback2"],
                        "client_name": "My Example Client",
                        "client_name#ja-JP":
                            "\u30AF\u30E9\u30A4\u30A2\u30F3\u30C8\u540D",
                        "token_endpoint_auth_method": "client_secret_basic",
                        "logo_uri": "https://client.example.org/logo.png",
                        "jwks_uri": "https://client.example.org/my_public_keys.jwks"
                    }
                ]
            })

    redirect_uris: list[HttpsUrl] | None = Field(
            description="Array of redirection URI strings for use in redirect-based flows "
                        "such as the authorization code and implicit flows.",
            placeholder="https://sub.example.com")

    token_endpoint_auth_method: Literal["none", "client_secret_post", "client_secret_basic"] = Field(
            description="String indicator of the requested authentication method for the token endpoint. "
                        "Possible values are: \"none\", \"client_secret_post\", \"client_secret_basic\". "
                        "If not provided, the default is \"client_secret_basic\"",
            default="client_secret_basic",
            placeholder="client_secret_basic")

    grant_types: list[GrantTypes] = Field(
            description="Array of OAuth 2.0 grant type strings that the client can use at the token endpoint",
            default=["client_secret_basic"],
            placeholder="client_secret_basic")

    response_types: list[ResponseTypes] = Field(
            description="Array of the OAuth 2.0 response type strings that the client can use at the authorization endpoint.",
            default=["code"],
            placeholder="code")

    client_name: str | None = Field(
            description="Human-readable string name of the client to be presented to the end-user during authorization.",
            default=None,
            placeholder="Client name")

    client_uri: HttpsUrl | None = Field(description="URL string of a web page providing information about the client.",
                                        default=None,
                                        placeholder="https://sub.example.com")

    logo_uri: HttpsUrl | None = Field(description="URL string that references a logo for the client.",
                                      default=None,
                                      placeholder="https://sub.example.com")

    scope: str = Field(
            description="String containing a space-separated list of scope values that the client can use when requesting access tokens.",
            default="",
            placeholder="openid scope1 scope2")

    contacts: list[str] | None = Field(
            description="Array of strings representing ways to contact people responsible for this client, typically email addresses.",
            default=None,
            placeholder="mail@example.com 88005553535")

    tos_uri: HttpsUrl | None = Field(description="URL string that points to a human-readable terms of service "
                                                 "document for the client that describes a contractual relationship "
                                                 "between the end-user and the client that the end-user accepts when "
                                                 "authorizing the client.",
                                     default=None,
                                     placeholder="https://sub.example.com")

    policy_uri: HttpsUrl | None = Field(
            description="URL string that points to a human-readable privacy policy document "
                        "that describes how the deployment organization collects, uses, "
                        "retains, and discloses personal data.",
            default=None,
            placeholder="https://sub.example.com")

    jwks_uri: HttpsUrl | None = Field(
            description="URL string referencing the client's JSON Web Key (JWK) Set document, "
                        "which contains the client's public keys. The \"jwks_uri\" and \"jwks\" "
                        "parameters MUST NOT both be present in the same request or response",
            default=None,
            placeholder="https://sub.example.com")

    jwks: list[JWK] | None = Field(
            description="Client's JSON Web Key Set [RFC7517] document value, which contains the client's public keys. "
                        "The \"jwks_uri\" and \"jwks\" parameters MUST NOT both be present in the same request or response",
            default=None,
            placeholder="jwks")

    software_id: UUID4 | None = Field(description="A UUID assigned by the client developer or software publisher "
                                                  "used by registration endpoints to identify the client software to "
                                                  "be dynamically registered.",
                                      default=None,
                                      placeholder="4a07437d-a56c-4789-82ac-5005bd2ab694")

    software_version: str | None = Field(
            description="A version identifier string for the client software identified by \"software_id\".",
            default=None,
            placeholder="1.0.0")

    software_statement: str | None = Field(description="A digitally signed or MACed JSON Web Token (JWT) that "
                                                       "asserts metadata values about the client software.",
                                           default=None,
                                           placeholder="secret_string_from_vendor")


class ClientInformationMin(ClientRegistrationRequest):
    client_id: UUID4


class ClientInformationResponse(ClientInformationMin):
    client_secret: str | None = None
    client_id_issued_at: NaiveDatetime | None = None
    client_secret_expires_at: NaiveDatetime | None = None
