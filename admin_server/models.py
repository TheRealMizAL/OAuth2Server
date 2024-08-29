import enum

from tortoise import Model, fields


class Users(Model):
    id = fields.UUIDField(pk=True)
    name = fields.CharField(max_length=64, null=True)
    surname = fields.CharField(max_length=64, null=True)
    patronymic = fields.CharField(max_length=64, null=True)

    creds: fields.ReverseRelation["Creds"]


class Creds(Model):
    user: fields.ForeignKeyRelation[Users] = fields.ForeignKeyField('main.Users', 'creds', pk=True)
    login = fields.CharField(max_length=255)
    passwd = fields.CharField(max_length=60)


class TokenEndpointAuthMethodsEnum(enum.Enum):
    NONE = "none"
    CLIENT_SECRET_POST = "client_secret_post"
    CLIENT_SECRET_BASIC = "client_secret_basic"


class GrantTypesEnum(enum.Enum):
    AUTHORIZATION_CODE = "authorization_code"
    IMPLICIT = "implicit"
    PASSWORD = "password"
    CLIENT_CREDENTIALS = "client_credentials"
    REFRESH_TOKEN = "refresh_token"
    JWT_BEARER = "urn:ietf:params:oauth:grant-type:jwt-bearer"
    SAML_BEARER = "urn:ietf:params:oauth:grant-type:saml2-bearer"


class ResponseTypesEnum(enum.Enum):
    CODE = "code"
    TOKEN = "token"


class Clients(Model):
    client_id = fields.UUIDField(pk=True,
                                 description="OAuth 2.0 client identifier string.")

    client_id_issued_at = fields.DatetimeField(auto_now_add=True, null=False)
    client_secret = fields.CharField(max_length=2048, null=True)
    client_secret_expires_at = fields.DatetimeField(null=True)

    token_endpoint_auth_method = fields.CharEnumField(
            TokenEndpointAuthMethodsEnum,
            description="String indicator of the requested authentication method for the token endpoint. "
                        "Possible values are: \"none\", \"client_secret_post\", \"client_secret_basic\". "
                        "If not provided, the default is \"client_secret_basic\"",
            default="client_secret_basic")

    scope = fields.CharField(max_length=255,
                             description="String containing a space-separated list of scope values that the client can use when requesting access tokens.",
                             default="")

    jwks_uri = fields.CharField(max_length=255,
                                description="URL string referencing the client's JSON Web Key (JWK) Set document, "
                                            "which contains the client's public keys. The \"jwks_uri\" and \"jwks\" "
                                            "parameters MUST NOT both be present in the same request or response",
                                default=None, null=True)

    software_id = fields.UUIDField(description="A UUID assigned by the client developer or software publisher "
                                               "used by registration endpoints to identify the client software to "
                                               "be dynamically registered.",
                                   default=None, null=True)

    software_version = fields.CharField(max_length=255,
                                        description="A version identifier string "
                                                    "for the client software identified by \"software_id\".",
                                        default=None, null=True)

    redirect_uris: fields.ReverseRelation["RedirectURIs"]
    grant_types: fields.ReverseRelation["GrantTypes"]
    response_types: fields.ReverseRelation["ResponseTypes"]
    contacts: fields.ReverseRelation["Contacts"]
    jwks: fields.ReverseRelation["JWKs"]

    tos_uris: fields.ReverseRelation["TOSURI"]
    client_names: fields.ReverseRelation["ClientName"]
    policy_uris: fields.ReverseRelation["PolicyURI"]
    logo_uris: fields.ReverseRelation["LogoURI"]
    client_uris: fields.ReverseRelation["ClientURI"]


class RedirectURIs(Model):
    client: fields.ForeignKeyRelation[Clients] = fields.ForeignKeyField('main.Clients', 'redirect_uris')
    redirect_uri = fields.CharField(max_length=255,
                                    description="Array of redirection URI strings for use in redirect-based flows "
                                                "such as the authorization code and implicit flows.")

    class Meta:
        unique_together = (('client_id', 'redirect_uri'),)


class GrantTypes(Model):
    client: fields.ForeignKeyRelation[Clients] = fields.ForeignKeyField('main.Clients', 'grant_types')
    grant_type = fields.CharEnumField(GrantTypesEnum,
                                      description="Array of OAuth 2.0 grant type strings "
                                                  "that the client can use at the token endpoint",
                                      default=GrantTypesEnum.AUTHORIZATION_CODE)

    class Meta:
        unique_together = (('client_id', 'grant_type'),)


class ResponseTypes(Model):
    client: fields.ForeignKeyRelation[Clients] = fields.ForeignKeyField('main.Clients', 'response_types')
    response_type = fields.CharEnumField(ResponseTypesEnum,
                                         description="Array of the OAuth 2.0 response type strings "
                                                     "that the client can use at the authorization endpoint.",
                                         default=ResponseTypesEnum.CODE)

    class Meta:
        unique_together = (('client_id', 'response_type'),)


class Contacts(Model):
    client: fields.ForeignKeyRelation[Clients] = fields.ForeignKeyField('main.Clients', 'contacts')
    contact = fields.CharField(max_length=255,
                               description="Array of strings representing ways to contact people "
                                           "responsible for this client, typically email addresses.",
                               default=None, null=True)

    class Meta:
        unique_together = (('client_id', 'contact'),)


class JWKs(Model):
    client: fields.ForeignKeyRelation[Clients] = fields.ForeignKeyField('main.Clients', 'jwks')
    jwk = fields.CharField(max_length=16384,
                           description="Client's JSON Web Key [RFC7517] document value, "
                                       "which contains the client's public keys. "
                                       "The \"jwks_uri\" and \"jwks\" parameters MUST NOT "
                                       "both be present in the same request or response",
                           default=None, null=True)

    class Meta:
        unique_together = (('client_id', 'jwk'),)


class ClientName(Model):
    client: fields.ForeignKeyRelation[Clients] = fields.ForeignKeyField('main.Clients', 'client_names', pk=True)
    client_name = fields.CharField(max_length=255,
                                   description="Human-readable string name of the client to be presented to the end-user during authorization.",
                                   default=None, null=True)
    client_name_af_za = fields.CharField(max_length=255, description="Client name (Afrikaans (South Africa))",
                                         default=None, null=True)
    client_name_ar_ae = fields.CharField(max_length=255, description="Client name (Arabic (U.A.E.))",
                                         default=None, null=True)
    client_name_ar_bh = fields.CharField(max_length=255, description="Client name (Arabic (Bahrain))",
                                         default=None, null=True)
    client_name_ar_dz = fields.CharField(max_length=255, description="Client name (Arabic (Algeria))",
                                         default=None, null=True)
    client_name_ar_eg = fields.CharField(max_length=255, description="Client name (Arabic (Egypt))",
                                         default=None, null=True)
    client_name_ar_iq = fields.CharField(max_length=255, description="Client name (Arabic (Iraq))",
                                         default=None, null=True)
    client_name_ar_jo = fields.CharField(max_length=255, description="Client name (Arabic (Jordan))",
                                         default=None, null=True)
    client_name_ar_kw = fields.CharField(max_length=255, description="Client name (Arabic (Kuwait))",
                                         default=None, null=True)
    client_name_ar_lb = fields.CharField(max_length=255, description="Client name (Arabic (Lebanon))",
                                         default=None, null=True)
    client_name_ar_ly = fields.CharField(max_length=255, description="Client name (Arabic (Libya))",
                                         default=None, null=True)
    client_name_ar_ma = fields.CharField(max_length=255, description="Client name (Arabic (Morocco))",
                                         default=None, null=True)
    client_name_ar_om = fields.CharField(max_length=255, description="Client name (Arabic (Oman))",
                                         default=None, null=True)
    client_name_ar_qa = fields.CharField(max_length=255, description="Client name (Arabic (Qatar))",
                                         default=None, null=True)
    client_name_ar_sa = fields.CharField(max_length=255, description="Client name (Arabic (Saudi Arabia))",
                                         default=None, null=True)
    client_name_ar_sy = fields.CharField(max_length=255, description="Client name (Arabic (Syria))",
                                         default=None, null=True)
    client_name_ar_tn = fields.CharField(max_length=255, description="Client name (Arabic (Tunisia))",
                                         default=None, null=True)
    client_name_ar_ye = fields.CharField(max_length=255, description="Client name (Arabic (Yemen))",
                                         default=None, null=True)
    client_name_az_az = fields.CharField(max_length=255,
                                         description="Client name (Azeri (Latin) (Azerbaijan))",
                                         default=None, null=True)
    client_name_az_cyrl_az = fields.CharField(max_length=255,
                                              description="Client name (Azeri (Cyrillic) (Azerbaijan))",
                                              default=None, null=True)
    client_name_be_by = fields.CharField(max_length=255, description="Client name (Belarusian (Belarus))",
                                         default=None, null=True)
    client_name_bg_bg = fields.CharField(max_length=255, description="Client name (Bulgarian (Bulgaria))",
                                         default=None, null=True)
    client_name_bs_ba = fields.CharField(max_length=255,
                                         description="Client name (Bosnian (Bosnia and Herzegovina))",
                                         default=None, null=True)
    client_name_ca_es = fields.CharField(max_length=255, description="Client name (Catalan (Spain))",
                                         default=None, null=True)
    client_name_cs_cz = fields.CharField(max_length=255, description="Client name (Czech (Czech Republic))",
                                         default=None, null=True)
    client_name_cy_gb = fields.CharField(max_length=255, description="Client name (Welsh (United Kingdom))",
                                         default=None, null=True)
    client_name_da_dk = fields.CharField(max_length=255, description="Client name (Danish (Denmark))",
                                         default=None, null=True)
    client_name_de_at = fields.CharField(max_length=255, description="Client name (German (Austria))",
                                         default=None, null=True)
    client_name_de_ch = fields.CharField(max_length=255, description="Client name (German (Switzerland))",
                                         default=None, null=True)
    client_name_de_de = fields.CharField(max_length=255, description="Client name (German (Germany))",
                                         default=None, null=True)
    client_name_de_li = fields.CharField(max_length=255, description="Client name (German (Liechtenstein))",
                                         default=None, null=True)
    client_name_de_lu = fields.CharField(max_length=255, description="Client name (German (Luxembourg))",
                                         default=None, null=True)
    client_name_dv_mv = fields.CharField(max_length=255, description="Client name (Divehi (Maldives))",
                                         default=None, null=True)
    client_name_el_gr = fields.CharField(max_length=255, description="Client name (Greek (Greece))",
                                         default=None, null=True)
    client_name_en_au = fields.CharField(max_length=255, description="Client name (English (Australia))",
                                         default=None, null=True)
    client_name_en_bz = fields.CharField(max_length=255, description="Client name (English (Belize))",
                                         default=None, null=True)
    client_name_en_ca = fields.CharField(max_length=255, description="Client name (English (Canada))",
                                         default=None, null=True)
    client_name_en_cb = fields.CharField(max_length=255, description="Client name (English (Caribbean))",
                                         default=None, null=True)
    client_name_en_gb = fields.CharField(max_length=255, description="Client name (English (United Kingdom))",
                                         default=None, null=True)
    client_name_en_ie = fields.CharField(max_length=255, description="Client name (English (Ireland))",
                                         default=None, null=True)
    client_name_en_jm = fields.CharField(max_length=255, description="Client name (English (Jamaica))",
                                         default=None, null=True)
    client_name_en_nz = fields.CharField(max_length=255, description="Client name (English (New Zealand))",
                                         default=None, null=True)
    client_name_en_ph = fields.CharField(max_length=255,
                                         description="Client name (English (Republic of the Philippines))",
                                         default=None, null=True)
    client_name_en_tt = fields.CharField(max_length=255,
                                         description="Client name (English (Trinidad and Tobago))", default=None,
                                         null=True)
    client_name_en_us = fields.CharField(max_length=255, description="Client name (English (United States))",
                                         default=None, null=True)
    client_name_en_za = fields.CharField(max_length=255, description="Client name (English (South Africa))",
                                         default=None, null=True)
    client_name_en_zw = fields.CharField(max_length=255, description="Client name (English (Zimbabwe))",
                                         default=None, null=True)
    client_name_es_ar = fields.CharField(max_length=255, description="Client name (Spanish (Argentina))",
                                         default=None, null=True)
    client_name_es_bo = fields.CharField(max_length=255, description="Client name (Spanish (Bolivia))",
                                         default=None, null=True)
    client_name_es_cl = fields.CharField(max_length=255, description="Client name (Spanish (Chile))",
                                         default=None, null=True)
    client_name_es_co = fields.CharField(max_length=255, description="Client name (Spanish (Colombia))",
                                         default=None, null=True)
    client_name_es_cr = fields.CharField(max_length=255, description="Client name (Spanish (Costa Rica))",
                                         default=None, null=True)
    client_name_es_do = fields.CharField(max_length=255,
                                         description="Client name (Spanish (Dominican Republic))",
                                         default=None, null=True)
    client_name_es_ec = fields.CharField(max_length=255, description="Client name (Spanish (Ecuador))",
                                         default=None, null=True)
    client_name_es_es = fields.CharField(max_length=255, description="Client name (Spanish (Spain))",
                                         default=None, null=True)
    client_name_es_gt = fields.CharField(max_length=255, description="Client name (Spanish (Guatemala))",
                                         default=None, null=True)
    client_name_es_hn = fields.CharField(max_length=255, description="Client name (Spanish (Honduras))",
                                         default=None, null=True)
    client_name_es_mx = fields.CharField(max_length=255, description="Client name (Spanish (Mexico))",
                                         default=None, null=True)
    client_name_es_ni = fields.CharField(max_length=255, description="Client name (Spanish (Nicaragua))",
                                         default=None, null=True)
    client_name_es_pa = fields.CharField(max_length=255, description="Client name (Spanish (Panama))",
                                         default=None, null=True)
    client_name_es_pe = fields.CharField(max_length=255, description="Client name (Spanish (Peru))",
                                         default=None, null=True)
    client_name_es_pr = fields.CharField(max_length=255, description="Client name (Spanish (Puerto Rico))",
                                         default=None, null=True)
    client_name_es_py = fields.CharField(max_length=255, description="Client name (Spanish (Paraguay))",
                                         default=None, null=True)
    client_name_es_sv = fields.CharField(max_length=255, description="Client name (Spanish (El Salvador))",
                                         default=None, null=True)
    client_name_es_uy = fields.CharField(max_length=255, description="Client name (Spanish (Uruguay))",
                                         default=None, null=True)
    client_name_es_ve = fields.CharField(max_length=255, description="Client name (Spanish (Venezuela))",
                                         default=None, null=True)
    client_name_et_ee = fields.CharField(max_length=255, description="Client name (Estonian (Estonia))",
                                         default=None, null=True)
    client_name_eu_es = fields.CharField(max_length=255, description="Client name (Basque (Spain))",
                                         default=None, null=True)
    client_name_fa_ir = fields.CharField(max_length=255, description="Client name (Farsi (Iran))",
                                         default=None, null=True)
    client_name_fi_fi = fields.CharField(max_length=255, description="Client name (Finnish (Finland))",
                                         default=None, null=True)
    client_name_fo_fo = fields.CharField(max_length=255, description="Client name (Faroese (Faroe Islands))",
                                         default=None, null=True)
    client_name_fr_be = fields.CharField(max_length=255, description="Client name (French (Belgium))",
                                         default=None, null=True)
    client_name_fr_ca = fields.CharField(max_length=255, description="Client name (French (Canada))",
                                         default=None, null=True)
    client_name_fr_ch = fields.CharField(max_length=255, description="Client name (French (Switzerland))",
                                         default=None, null=True)
    client_name_fr_fr = fields.CharField(max_length=255, description="Client name (French (France))",
                                         default=None, null=True)
    client_name_fr_lu = fields.CharField(max_length=255, description="Client name (French (Luxembourg))",
                                         default=None, null=True)
    client_name_fr_mc = fields.CharField(max_length=255,
                                         description="Client name (French (Principality of Monaco))", default=None,
                                         null=True)
    client_name_gl_es = fields.CharField(max_length=255, description="Client name (Galician (Spain))",
                                         default=None, null=True)
    client_name_gu_in = fields.CharField(max_length=255, description="Client name (Gujarati (India))",
                                         default=None, null=True)
    client_name_he_il = fields.CharField(max_length=255, description="Client name (Hebrew (Israel))",
                                         default=None, null=True)
    client_name_hi_in = fields.CharField(max_length=255, description="Client name (Hindi (India))",
                                         default=None, null=True)
    client_name_hr_ba = fields.CharField(max_length=255,
                                         description="Client name (Croatian (Bosnia and Herzegovina))",
                                         default=None, null=True)
    client_name_hr_hr = fields.CharField(max_length=255, description="Client name (Croatian (Croatia))",
                                         default=None, null=True)
    client_name_hu_hu = fields.CharField(max_length=255, description="Client name (Hungarian (Hungary))",
                                         default=None, null=True)
    client_name_hy_am = fields.CharField(max_length=255, description="Client name (Armenian (Armenia))",
                                         default=None, null=True)
    client_name_id_id = fields.CharField(max_length=255, description="Client name (Indonesian (Indonesia))",
                                         default=None, null=True)
    client_name_is_is = fields.CharField(max_length=255, description="Client name (Icelandic (Iceland))",
                                         default=None, null=True)
    client_name_it_ch = fields.CharField(max_length=255, description="Client name (Italian (Switzerland))",
                                         default=None, null=True)
    client_name_it_it = fields.CharField(max_length=255, description="Client name (Italian (Italy))",
                                         default=None, null=True)
    client_name_ja_jp = fields.CharField(max_length=255, description="Client name (Japanese (Japan))",
                                         default=None, null=True)
    client_name_ka_ge = fields.CharField(max_length=255, description="Client name (Georgian (Georgia))",
                                         default=None, null=True)
    client_name_kk_kz = fields.CharField(max_length=255, description="Client name (Kazakh (Kazakhstan))",
                                         default=None, null=True)
    client_name_kn_in = fields.CharField(max_length=255, description="Client name (Kannada (India))",
                                         default=None, null=True)
    client_name_ko_kr = fields.CharField(max_length=255, description="Client name (Korean (Korea))",
                                         default=None, null=True)
    client_name_kok_in = fields.CharField(max_length=255, description="Client name (Konkani (India))",
                                          default=None, null=True)
    client_name_ky_kg = fields.CharField(max_length=255, description="Client name (Kyrgyz (Kyrgyzstan))",
                                         default=None, null=True)
    client_name_lt_lt = fields.CharField(max_length=255, description="Client name (Lithuanian (Lithuania))",
                                         default=None, null=True)
    client_name_lv_lv = fields.CharField(max_length=255, description="Client name (Latvian (Latvia))",
                                         default=None, null=True)
    client_name_mi_nz = fields.CharField(max_length=255, description="Client name (Maori (New Zealand))",
                                         default=None, null=True)
    client_name_mk_mk = fields.CharField(max_length=255,
                                         description="Client name (FYRO Macedonian (Former Yugoslav Republic of Macedonia))",
                                         default=None, null=True)
    client_name_mn_mn = fields.CharField(max_length=255, description="Client name (Mongolian (Mongolia))",
                                         default=None, null=True)
    client_name_mr_in = fields.CharField(max_length=255, description="Client name (Marathi (India))",
                                         default=None, null=True)
    client_name_ms_bn = fields.CharField(max_length=255,
                                         description="Client name (Malay (Brunei Darussalam))",
                                         default=None, null=True)
    client_name_ms_my = fields.CharField(max_length=255, description="Client name (Malay (Malaysia))",
                                         default=None, null=True)
    client_name_mt_mt = fields.CharField(max_length=255, description="Client name (Maltese (Malta))",
                                         default=None, null=True)
    client_name_nb_no = fields.CharField(max_length=255,
                                         description="Client name (Norwegian (Bokm?l) (Norway))",
                                         default=None, null=True)
    client_name_nl_be = fields.CharField(max_length=255, description="Client name (Dutch (Belgium))",
                                         default=None, null=True)
    client_name_nl_nl = fields.CharField(max_length=255, description="Client name (Dutch (Netherlands))",
                                         default=None, null=True)
    client_name_nn_no = fields.CharField(max_length=255,
                                         description="Client name (Norwegian (Nynorsk) (Norway))",
                                         default=None, null=True)
    client_name_ns_za = fields.CharField(max_length=255,
                                         description="Client name (Northern Sotho (South Africa))", default=None,
                                         null=True)
    client_name_pa_in = fields.CharField(max_length=255, description="Client name (Punjabi (India))",
                                         default=None, null=True)
    client_name_pl_pl = fields.CharField(max_length=255, description="Client name (Polish (Poland))",
                                         default=None, null=True)
    client_name_ps_ar = fields.CharField(max_length=255, description="Client name (Pashto (Afghanistan))",
                                         default=None, null=True)
    client_name_pt_br = fields.CharField(max_length=255, description="Client name (Portuguese (Brazil))",
                                         default=None, null=True)
    client_name_pt_pt = fields.CharField(max_length=255, description="Client name (Portuguese (Portugal))",
                                         default=None, null=True)
    client_name_qu_bo = fields.CharField(max_length=255, description="Client name (Quechua (Bolivia))",
                                         default=None, null=True)
    client_name_qu_ec = fields.CharField(max_length=255, description="Client name (Quechua (Ecuador))",
                                         default=None, null=True)
    client_name_qu_pe = fields.CharField(max_length=255, description="Client name (Quechua (Peru))",
                                         default=None, null=True)
    client_name_ro_ro = fields.CharField(max_length=255, description="Client name (Romanian (Romania))",
                                         default=None, null=True)
    client_name_ru_ru = fields.CharField(max_length=255, description="Client name (Russian (Russia))",
                                         default=None, null=True)
    client_name_sa_in = fields.CharField(max_length=255, description="Client name (Sanskrit (India))",
                                         default=None, null=True)
    client_name_se_fi = fields.CharField(max_length=255, description="Client name (Sami (Finland))",
                                         default=None, null=True)
    client_name_se_no = fields.CharField(max_length=255, description="Client name (Sami (Norway))",
                                         default=None, null=True)
    client_name_se_se = fields.CharField(max_length=255, description="Client name (Sami (Sweden))",
                                         default=None, null=True)
    client_name_sk_sk = fields.CharField(max_length=255, description="Client name (Slovak (Slovakia))",
                                         default=None, null=True)
    client_name_sl_si = fields.CharField(max_length=255, description="Client name (Slovenian (Slovenia))",
                                         default=None, null=True)
    client_name_sq_al = fields.CharField(max_length=255, description="Client name (Albanian (Albania))",
                                         default=None, null=True)
    client_name_sr_ba = fields.CharField(max_length=255,
                                         description="Client name (Serbian (Latin) (Bosnia and Herzegovina))",
                                         default=None, null=True)
    client_name_sr_cyrl_ba = fields.CharField(max_length=255,
                                              description="Client name (Serbian (Cyrillic) (Bosnia and Herzegovina))",
                                              default=None, null=True)
    client_name_sr_sp = fields.CharField(max_length=255,
                                         description="Client name (Serbian (Latin) (Serbia and Montenegro))",
                                         default=None, null=True)
    client_name_sr_cyrl_sp = fields.CharField(max_length=255,
                                              description="Client name (Serbian (Cyrillic) (Serbia and Montenegro))",
                                              default=None, null=True)
    client_name_sv_fi = fields.CharField(max_length=255, description="Client name (Swedish (Finland))",
                                         default=None, null=True)
    client_name_sv_se = fields.CharField(max_length=255, description="Client name (Swedish (Sweden))",
                                         default=None, null=True)
    client_name_sw_ke = fields.CharField(max_length=255, description="Client name (Swahili (Kenya))",
                                         default=None, null=True)
    client_name_syr_sy = fields.CharField(max_length=255, description="Client name (Syriac (Syria))",
                                          default=None, null=True)
    client_name_ta_in = fields.CharField(max_length=255, description="Client name (Tamil (India))",
                                         default=None, null=True)
    client_name_te_in = fields.CharField(max_length=255, description="Client name (Telugu (India))",
                                         default=None, null=True)
    client_name_th_th = fields.CharField(max_length=255, description="Client name (Thai (Thailand))",
                                         default=None, null=True)
    client_name_tl_ph = fields.CharField(max_length=255, description="Client name (Tagalog (Philippines))",
                                         default=None, null=True)
    client_name_tn_za = fields.CharField(max_length=255, description="Client name (Tswana (South Africa))",
                                         default=None, null=True)
    client_name_tr_tr = fields.CharField(max_length=255, description="Client name (Turkish (Turkey))",
                                         default=None, null=True)
    client_name_tt_ru = fields.CharField(max_length=255, description="Client name (Tatar (Russia))",
                                         default=None, null=True)
    client_name_uk_ua = fields.CharField(max_length=255, description="Client name (Ukrainian (Ukraine))",
                                         default=None, null=True)
    client_name_ur_pk = fields.CharField(max_length=255,
                                         description="Client name (Urdu (Islamic Republic of Pakistan))",
                                         default=None, null=True)
    client_name_uz_uz = fields.CharField(max_length=255,
                                         description="Client name (Uzbek (Latin) (Uzbekistan))",
                                         default=None, null=True)
    client_name_uz_cyrl_uz = fields.CharField(max_length=255,
                                              description="Client name (Uzbek (Cyrillic) (Uzbekistan))",
                                              default=None, null=True)
    client_name_vi_vn = fields.CharField(max_length=255, description="Client name (Vietnamese (Viet Nam))",
                                         default=None, null=True)
    client_name_xh_za = fields.CharField(max_length=255, description="Client name (Xhosa (South Africa))",
                                         default=None, null=True)
    client_name_zh_cn = fields.CharField(max_length=255, description="Client name (Chinese (S))",
                                         default=None, null=True)
    client_name_zh_hk = fields.CharField(max_length=255, description="Client name (Chinese (Hong Kong))",
                                         default=None, null=True)
    client_name_zh_mo = fields.CharField(max_length=255, description="Client name (Chinese (Macau))",
                                         default=None, null=True)
    client_name_zh_sg = fields.CharField(max_length=255, description="Client name (Chinese (Singapore))",
                                         default=None, null=True)
    client_name_zh_tw = fields.CharField(max_length=255, description="Client name (Chinese (T))",
                                         default=None, null=True)
    client_name_zu_za = fields.CharField(max_length=255, description="Client name (Zulu (South Africa))",
                                         default=None, null=True)


class TOSURI(Model):
    client: fields.ForeignKeyRelation[Clients] = fields.ForeignKeyField('main.Clients', 'tos_uris', pk=True)
    tos_uri = fields.CharField(max_length=255,
                               description="URL string that points to a human-readable terms of service "
                                           "document for the client that describes a contractual relationship "
                                           "between the end-user and the client that the end-user accepts when "
                                           "authorizing the client.",
                               default=None, null=True)

    tos_uri_af_za = fields.CharField(max_length=255, description="ToS URI (Afrikaans (South Africa))",
                                     default=None, null=True)
    tos_uri_ar_ae = fields.CharField(max_length=255, description="ToS URI (Arabic (U.A.E.))", default=None,
                                     null=True)
    tos_uri_ar_bh = fields.CharField(max_length=255, description="ToS URI (Arabic (Bahrain))", default=None,
                                     null=True)
    tos_uri_ar_dz = fields.CharField(max_length=255, description="ToS URI (Arabic (Algeria))", default=None,
                                     null=True)
    tos_uri_ar_eg = fields.CharField(max_length=255, description="ToS URI (Arabic (Egypt))", default=None,
                                     null=True)
    tos_uri_ar_iq = fields.CharField(max_length=255, description="ToS URI (Arabic (Iraq))", default=None,
                                     null=True)
    tos_uri_ar_jo = fields.CharField(max_length=255, description="ToS URI (Arabic (Jordan))", default=None,
                                     null=True)
    tos_uri_ar_kw = fields.CharField(max_length=255, description="ToS URI (Arabic (Kuwait))", default=None,
                                     null=True)
    tos_uri_ar_lb = fields.CharField(max_length=255, description="ToS URI (Arabic (Lebanon))", default=None,
                                     null=True)
    tos_uri_ar_ly = fields.CharField(max_length=255, description="ToS URI (Arabic (Libya))", default=None,
                                     null=True)
    tos_uri_ar_ma = fields.CharField(max_length=255, description="ToS URI (Arabic (Morocco))", default=None,
                                     null=True)
    tos_uri_ar_om = fields.CharField(max_length=255, description="ToS URI (Arabic (Oman))", default=None,
                                     null=True)
    tos_uri_ar_qa = fields.CharField(max_length=255, description="ToS URI (Arabic (Qatar))", default=None,
                                     null=True)
    tos_uri_ar_sa = fields.CharField(max_length=255, description="ToS URI (Arabic (Saudi Arabia))", default=None,
                                     null=True)
    tos_uri_ar_sy = fields.CharField(max_length=255, description="ToS URI (Arabic (Syria))", default=None,
                                     null=True)
    tos_uri_ar_tn = fields.CharField(max_length=255, description="ToS URI (Arabic (Tunisia))", default=None,
                                     null=True)
    tos_uri_ar_ye = fields.CharField(max_length=255, description="ToS URI (Arabic (Yemen))", default=None,
                                     null=True)
    tos_uri_az_az = fields.CharField(max_length=255, description="ToS URI (Azeri (Latin) (Azerbaijan))",
                                     default=None, null=True)
    tos_uri_az_cyrl_az = fields.CharField(max_length=255,
                                          description="ToS URI (Azeri (Cyrillic) (Azerbaijan))",
                                          default=None, null=True)
    tos_uri_be_by = fields.CharField(max_length=255, description="ToS URI (Belarusian (Belarus))", default=None,
                                     null=True)
    tos_uri_bg_bg = fields.CharField(max_length=255, description="ToS URI (Bulgarian (Bulgaria))", default=None,
                                     null=True)
    tos_uri_bs_ba = fields.CharField(max_length=255, description="ToS URI (Bosnian (Bosnia and Herzegovina))",
                                     default=None, null=True)
    tos_uri_ca_es = fields.CharField(max_length=255, description="ToS URI (Catalan (Spain))", default=None,
                                     null=True)
    tos_uri_cs_cz = fields.CharField(max_length=255, description="ToS URI (Czech (Czech Republic))", default=None,
                                     null=True)
    tos_uri_cy_gb = fields.CharField(max_length=255, description="ToS URI (Welsh (United Kingdom))", default=None,
                                     null=True)
    tos_uri_da_dk = fields.CharField(max_length=255, description="ToS URI (Danish (Denmark))", default=None,
                                     null=True)
    tos_uri_de_at = fields.CharField(max_length=255, description="ToS URI (German (Austria))", default=None,
                                     null=True)
    tos_uri_de_ch = fields.CharField(max_length=255, description="ToS URI (German (Switzerland))", default=None,
                                     null=True)
    tos_uri_de_de = fields.CharField(max_length=255, description="ToS URI (German (Germany))", default=None,
                                     null=True)
    tos_uri_de_li = fields.CharField(max_length=255, description="ToS URI (German (Liechtenstein))", default=None,
                                     null=True)
    tos_uri_de_lu = fields.CharField(max_length=255, description="ToS URI (German (Luxembourg))", default=None,
                                     null=True)
    tos_uri_dv_mv = fields.CharField(max_length=255, description="ToS URI (Divehi (Maldives))", default=None,
                                     null=True)
    tos_uri_el_gr = fields.CharField(max_length=255, description="ToS URI (Greek (Greece))", default=None,
                                     null=True)
    tos_uri_en_au = fields.CharField(max_length=255, description="ToS URI (English (Australia))", default=None,
                                     null=True)
    tos_uri_en_bz = fields.CharField(max_length=255, description="ToS URI (English (Belize))", default=None,
                                     null=True)
    tos_uri_en_ca = fields.CharField(max_length=255, description="ToS URI (English (Canada))", default=None,
                                     null=True)
    tos_uri_en_cb = fields.CharField(max_length=255, description="ToS URI (English (Caribbean))", default=None,
                                     null=True)
    tos_uri_en_gb = fields.CharField(max_length=255, description="ToS URI (English (United Kingdom))",
                                     default=None, null=True)
    tos_uri_en_ie = fields.CharField(max_length=255, description="ToS URI (English (Ireland))", default=None,
                                     null=True)
    tos_uri_en_jm = fields.CharField(max_length=255, description="ToS URI (English (Jamaica))", default=None,
                                     null=True)
    tos_uri_en_nz = fields.CharField(max_length=255, description="ToS URI (English (New Zealand))", default=None,
                                     null=True)
    tos_uri_en_ph = fields.CharField(max_length=255,
                                     description="ToS URI (English (Republic of the Philippines))",
                                     default=None, null=True)
    tos_uri_en_tt = fields.CharField(max_length=255, description="ToS URI (English (Trinidad and Tobago))",
                                     default=None, null=True)
    tos_uri_en_us = fields.CharField(max_length=255, description="ToS URI (English (United States))",
                                     default=None, null=True)
    tos_uri_en_za = fields.CharField(max_length=255, description="ToS URI (English (South Africa))", default=None,
                                     null=True)
    tos_uri_en_zw = fields.CharField(max_length=255, description="ToS URI (English (Zimbabwe))", default=None,
                                     null=True)
    tos_uri_es_ar = fields.CharField(max_length=255, description="ToS URI (Spanish (Argentina))", default=None,
                                     null=True)
    tos_uri_es_bo = fields.CharField(max_length=255, description="ToS URI (Spanish (Bolivia))", default=None,
                                     null=True)
    tos_uri_es_cl = fields.CharField(max_length=255, description="ToS URI (Spanish (Chile))", default=None,
                                     null=True)
    tos_uri_es_co = fields.CharField(max_length=255, description="ToS URI (Spanish (Colombia))", default=None,
                                     null=True)
    tos_uri_es_cr = fields.CharField(max_length=255, description="ToS URI (Spanish (Costa Rica))", default=None,
                                     null=True)
    tos_uri_es_do = fields.CharField(max_length=255, description="ToS URI (Spanish (Dominican Republic))",
                                     default=None, null=True)
    tos_uri_es_ec = fields.CharField(max_length=255, description="ToS URI (Spanish (Ecuador))", default=None,
                                     null=True)
    tos_uri_es_es = fields.CharField(max_length=255, description="ToS URI (Spanish (Spain))", default=None,
                                     null=True)
    tos_uri_es_gt = fields.CharField(max_length=255, description="ToS URI (Spanish (Guatemala))", default=None,
                                     null=True)
    tos_uri_es_hn = fields.CharField(max_length=255, description="ToS URI (Spanish (Honduras))", default=None,
                                     null=True)
    tos_uri_es_mx = fields.CharField(max_length=255, description="ToS URI (Spanish (Mexico))", default=None,
                                     null=True)
    tos_uri_es_ni = fields.CharField(max_length=255, description="ToS URI (Spanish (Nicaragua))", default=None,
                                     null=True)
    tos_uri_es_pa = fields.CharField(max_length=255, description="ToS URI (Spanish (Panama))", default=None,
                                     null=True)
    tos_uri_es_pe = fields.CharField(max_length=255, description="ToS URI (Spanish (Peru))", default=None,
                                     null=True)
    tos_uri_es_pr = fields.CharField(max_length=255, description="ToS URI (Spanish (Puerto Rico))", default=None,
                                     null=True)
    tos_uri_es_py = fields.CharField(max_length=255, description="ToS URI (Spanish (Paraguay))", default=None,
                                     null=True)
    tos_uri_es_sv = fields.CharField(max_length=255, description="ToS URI (Spanish (El Salvador))", default=None,
                                     null=True)
    tos_uri_es_uy = fields.CharField(max_length=255, description="ToS URI (Spanish (Uruguay))", default=None,
                                     null=True)
    tos_uri_es_ve = fields.CharField(max_length=255, description="ToS URI (Spanish (Venezuela))", default=None,
                                     null=True)
    tos_uri_et_ee = fields.CharField(max_length=255, description="ToS URI (Estonian (Estonia))", default=None,
                                     null=True)
    tos_uri_eu_es = fields.CharField(max_length=255, description="ToS URI (Basque (Spain))", default=None,
                                     null=True)
    tos_uri_fa_ir = fields.CharField(max_length=255, description="ToS URI (Farsi (Iran))", default=None, null=True)
    tos_uri_fi_fi = fields.CharField(max_length=255, description="ToS URI (Finnish (Finland))", default=None,
                                     null=True)
    tos_uri_fo_fo = fields.CharField(max_length=255, description="ToS URI (Faroese (Faroe Islands))",
                                     default=None, null=True)
    tos_uri_fr_be = fields.CharField(max_length=255, description="ToS URI (French (Belgium))", default=None,
                                     null=True)
    tos_uri_fr_ca = fields.CharField(max_length=255, description="ToS URI (French (Canada))", default=None,
                                     null=True)
    tos_uri_fr_ch = fields.CharField(max_length=255, description="ToS URI (French (Switzerland))", default=None,
                                     null=True)
    tos_uri_fr_fr = fields.CharField(max_length=255, description="ToS URI (French (France))", default=None,
                                     null=True)
    tos_uri_fr_lu = fields.CharField(max_length=255, description="ToS URI (French (Luxembourg))", default=None,
                                     null=True)
    tos_uri_fr_mc = fields.CharField(max_length=255, description="ToS URI (French (Principality of Monaco))",
                                     default=None, null=True)
    tos_uri_gl_es = fields.CharField(max_length=255, description="ToS URI (Galician (Spain))", default=None,
                                     null=True)
    tos_uri_gu_in = fields.CharField(max_length=255, description="ToS URI (Gujarati (India))", default=None,
                                     null=True)
    tos_uri_he_il = fields.CharField(max_length=255, description="ToS URI (Hebrew (Israel))", default=None,
                                     null=True)
    tos_uri_hi_in = fields.CharField(max_length=255, description="ToS URI (Hindi (India))", default=None,
                                     null=True)
    tos_uri_hr_ba = fields.CharField(max_length=255, description="ToS URI (Croatian (Bosnia and Herzegovina))",
                                     default=None, null=True)
    tos_uri_hr_hr = fields.CharField(max_length=255, description="ToS URI (Croatian (Croatia))", default=None,
                                     null=True)
    tos_uri_hu_hu = fields.CharField(max_length=255, description="ToS URI (Hungarian (Hungary))", default=None,
                                     null=True)
    tos_uri_hy_am = fields.CharField(max_length=255, description="ToS URI (Armenian (Armenia))", default=None,
                                     null=True)
    tos_uri_id_id = fields.CharField(max_length=255, description="ToS URI (Indonesian (Indonesia))", default=None,
                                     null=True)
    tos_uri_is_is = fields.CharField(max_length=255, description="ToS URI (Icelandic (Iceland))", default=None,
                                     null=True)
    tos_uri_it_ch = fields.CharField(max_length=255, description="ToS URI (Italian (Switzerland))", default=None,
                                     null=True)
    tos_uri_it_it = fields.CharField(max_length=255, description="ToS URI (Italian (Italy))", default=None,
                                     null=True)
    tos_uri_ja_jp = fields.CharField(max_length=255, description="ToS URI (Japanese (Japan))", default=None,
                                     null=True)
    tos_uri_ka_ge = fields.CharField(max_length=255, description="ToS URI (Georgian (Georgia))", default=None,
                                     null=True)
    tos_uri_kk_kz = fields.CharField(max_length=255, description="ToS URI (Kazakh (Kazakhstan))", default=None,
                                     null=True)
    tos_uri_kn_in = fields.CharField(max_length=255, description="ToS URI (Kannada (India))", default=None,
                                     null=True)
    tos_uri_ko_kr = fields.CharField(max_length=255, description="ToS URI (Korean (Korea))", default=None,
                                     null=True)
    tos_uri_kok_in = fields.CharField(max_length=255, description="ToS URI (Konkani (India))", default=None,
                                      null=True)
    tos_uri_ky_kg = fields.CharField(max_length=255, description="ToS URI (Kyrgyz (Kyrgyzstan))", default=None,
                                     null=True)
    tos_uri_lt_lt = fields.CharField(max_length=255, description="ToS URI (Lithuanian (Lithuania))", default=None,
                                     null=True)
    tos_uri_lv_lv = fields.CharField(max_length=255, description="ToS URI (Latvian (Latvia))", default=None,
                                     null=True)
    tos_uri_mi_nz = fields.CharField(max_length=255, description="ToS URI (Maori (New Zealand))", default=None,
                                     null=True)
    tos_uri_mk_mk = fields.CharField(max_length=255,
                                     description="ToS URI (FYRO Macedonian (Former Yugoslav Republic of Macedonia))",
                                     default=None, null=True)
    tos_uri_mn_mn = fields.CharField(max_length=255, description="ToS URI (Mongolian (Mongolia))", default=None,
                                     null=True)
    tos_uri_mr_in = fields.CharField(max_length=255, description="ToS URI (Marathi (India))", default=None,
                                     null=True)
    tos_uri_ms_bn = fields.CharField(max_length=255, description="ToS URI (Malay (Brunei Darussalam))",
                                     default=None, null=True)
    tos_uri_ms_my = fields.CharField(max_length=255, description="ToS URI (Malay (Malaysia))", default=None,
                                     null=True)
    tos_uri_mt_mt = fields.CharField(max_length=255, description="ToS URI (Maltese (Malta))", default=None,
                                     null=True)
    tos_uri_nb_no = fields.CharField(max_length=255, description="ToS URI (Norwegian (Bokm?l) (Norway))",
                                     default=None, null=True)
    tos_uri_nl_be = fields.CharField(max_length=255, description="ToS URI (Dutch (Belgium))", default=None,
                                     null=True)
    tos_uri_nl_nl = fields.CharField(max_length=255, description="ToS URI (Dutch (Netherlands))", default=None,
                                     null=True)
    tos_uri_nn_no = fields.CharField(max_length=255, description="ToS URI (Norwegian (Nynorsk) (Norway))",
                                     default=None, null=True)
    tos_uri_ns_za = fields.CharField(max_length=255, description="ToS URI (Northern Sotho (South Africa))",
                                     default=None, null=True)
    tos_uri_pa_in = fields.CharField(max_length=255, description="ToS URI (Punjabi (India))", default=None,
                                     null=True)
    tos_uri_pl_pl = fields.CharField(max_length=255, description="ToS URI (Polish (Poland))", default=None,
                                     null=True)
    tos_uri_ps_ar = fields.CharField(max_length=255, description="ToS URI (Pashto (Afghanistan))", default=None,
                                     null=True)
    tos_uri_pt_br = fields.CharField(max_length=255, description="ToS URI (Portuguese (Brazil))", default=None,
                                     null=True)
    tos_uri_pt_pt = fields.CharField(max_length=255, description="ToS URI (Portuguese (Portugal))", default=None,
                                     null=True)
    tos_uri_qu_bo = fields.CharField(max_length=255, description="ToS URI (Quechua (Bolivia))", default=None,
                                     null=True)
    tos_uri_qu_ec = fields.CharField(max_length=255, description="ToS URI (Quechua (Ecuador))", default=None,
                                     null=True)
    tos_uri_qu_pe = fields.CharField(max_length=255, description="ToS URI (Quechua (Peru))", default=None,
                                     null=True)
    tos_uri_ro_ro = fields.CharField(max_length=255, description="ToS URI (Romanian (Romania))", default=None,
                                     null=True)
    tos_uri_ru_ru = fields.CharField(max_length=255, description="ToS URI (Russian (Russia))", default=None,
                                     null=True)
    tos_uri_sa_in = fields.CharField(max_length=255, description="ToS URI (Sanskrit (India))", default=None,
                                     null=True)
    tos_uri_se_fi = fields.CharField(max_length=255, description="ToS URI (Sami (Finland))", default=None,
                                     null=True)
    tos_uri_se_no = fields.CharField(max_length=255, description="ToS URI (Sami (Norway))", default=None,
                                     null=True)
    tos_uri_se_se = fields.CharField(max_length=255, description="ToS URI (Sami (Sweden))", default=None,
                                     null=True)
    tos_uri_sk_sk = fields.CharField(max_length=255, description="ToS URI (Slovak (Slovakia))", default=None,
                                     null=True)
    tos_uri_sl_si = fields.CharField(max_length=255, description="ToS URI (Slovenian (Slovenia))", default=None,
                                     null=True)
    tos_uri_sq_al = fields.CharField(max_length=255, description="ToS URI (Albanian (Albania))", default=None,
                                     null=True)
    tos_uri_sr_ba = fields.CharField(max_length=255,
                                     description="ToS URI (Serbian (Latin) (Bosnia and Herzegovina))",
                                     default=None, null=True)
    tos_uri_sr_cyrl_ba = fields.CharField(max_length=255,
                                          description="ToS URI (Serbian (Cyrillic) (Bosnia and Herzegovina))",
                                          default=None, null=True)
    tos_uri_sr_sp = fields.CharField(max_length=255,
                                     description="ToS URI (Serbian (Latin) (Serbia and Montenegro))",
                                     default=None, null=True)
    tos_uri_sr_cyrl_sp = fields.CharField(max_length=255,
                                          description="ToS URI (Serbian (Cyrillic) (Serbia and Montenegro))",
                                          default=None, null=True)
    tos_uri_sv_fi = fields.CharField(max_length=255, description="ToS URI (Swedish (Finland))", default=None,
                                     null=True)
    tos_uri_sv_se = fields.CharField(max_length=255, description="ToS URI (Swedish (Sweden))", default=None,
                                     null=True)
    tos_uri_sw_ke = fields.CharField(max_length=255, description="ToS URI (Swahili (Kenya))", default=None,
                                     null=True)
    tos_uri_syr_sy = fields.CharField(max_length=255, description="ToS URI (Syriac (Syria))", default=None,
                                      null=True)
    tos_uri_ta_in = fields.CharField(max_length=255, description="ToS URI (Tamil (India))", default=None,
                                     null=True)
    tos_uri_te_in = fields.CharField(max_length=255, description="ToS URI (Telugu (India))", default=None,
                                     null=True)
    tos_uri_th_th = fields.CharField(max_length=255, description="ToS URI (Thai (Thailand))", default=None,
                                     null=True)
    tos_uri_tl_ph = fields.CharField(max_length=255, description="ToS URI (Tagalog (Philippines))", default=None,
                                     null=True)
    tos_uri_tn_za = fields.CharField(max_length=255, description="ToS URI (Tswana (South Africa))", default=None,
                                     null=True)
    tos_uri_tr_tr = fields.CharField(max_length=255, description="ToS URI (Turkish (Turkey))", default=None,
                                     null=True)
    tos_uri_tt_ru = fields.CharField(max_length=255, description="ToS URI (Tatar (Russia))", default=None,
                                     null=True)
    tos_uri_uk_ua = fields.CharField(max_length=255, description="ToS URI (Ukrainian (Ukraine))", default=None,
                                     null=True)
    tos_uri_ur_pk = fields.CharField(max_length=255, description="ToS URI (Urdu (Islamic Republic of Pakistan))",
                                     default=None, null=True)
    tos_uri_uz_uz = fields.CharField(max_length=255, description="ToS URI (Uzbek (Latin) (Uzbekistan))",
                                     default=None, null=True)
    tos_uri_uz_cyrl_uz = fields.CharField(max_length=255,
                                          description="ToS URI (Uzbek (Cyrillic) (Uzbekistan))",
                                          default=None, null=True)
    tos_uri_vi_vn = fields.CharField(max_length=255, description="ToS URI (Vietnamese (Viet Nam))", default=None,
                                     null=True)
    tos_uri_xh_za = fields.CharField(max_length=255, description="ToS URI (Xhosa (South Africa))", default=None,
                                     null=True)
    tos_uri_zh_cn = fields.CharField(max_length=255, description="ToS URI (Chinese (S))", default=None, null=True)
    tos_uri_zh_hk = fields.CharField(max_length=255, description="ToS URI (Chinese (Hong Kong))", default=None,
                                     null=True)
    tos_uri_zh_mo = fields.CharField(max_length=255, description="ToS URI (Chinese (Macau))", default=None,
                                     null=True)
    tos_uri_zh_sg = fields.CharField(max_length=255, description="ToS URI (Chinese (Singapore))", default=None,
                                     null=True)
    tos_uri_zh_tw = fields.CharField(max_length=255, description="ToS URI (Chinese (T))", default=None, null=True)
    tos_uri_zu_za = fields.CharField(max_length=255, description="ToS URI (Zulu (South Africa))", default=None,
                                     null=True)


class PolicyURI(Model):
    client: fields.ForeignKeyRelation[Clients] = fields.ForeignKeyField('main.Clients', 'policy_uris', pk=True)
    policy_uri = fields.CharField(max_length=255,
                                  description="URL string that points to a human-readable privacy policy document "
                                              "that describes how the deployment organization collects, uses, "
                                              "retains, and discloses personal data.",
                                  default=None, null=True)

    policy_uri_af_za = fields.CharField(max_length=255, description="Policy URI (Afrikaans (South Africa))",
                                        default=None, null=True)
    policy_uri_ar_ae = fields.CharField(max_length=255, description="Policy URI (Arabic (U.A.E.))",
                                        default=None, null=True)
    policy_uri_ar_bh = fields.CharField(max_length=255, description="Policy URI (Arabic (Bahrain))",
                                        default=None, null=True)
    policy_uri_ar_dz = fields.CharField(max_length=255, description="Policy URI (Arabic (Algeria))",
                                        default=None, null=True)
    policy_uri_ar_eg = fields.CharField(max_length=255, description="Policy URI (Arabic (Egypt))",
                                        default=None, null=True)
    policy_uri_ar_iq = fields.CharField(max_length=255, description="Policy URI (Arabic (Iraq))", default=None,
                                        null=True)
    policy_uri_ar_jo = fields.CharField(max_length=255, description="Policy URI (Arabic (Jordan))",
                                        default=None, null=True)
    policy_uri_ar_kw = fields.CharField(max_length=255, description="Policy URI (Arabic (Kuwait))",
                                        default=None, null=True)
    policy_uri_ar_lb = fields.CharField(max_length=255, description="Policy URI (Arabic (Lebanon))",
                                        default=None, null=True)
    policy_uri_ar_ly = fields.CharField(max_length=255, description="Policy URI (Arabic (Libya))",
                                        default=None, null=True)
    policy_uri_ar_ma = fields.CharField(max_length=255, description="Policy URI (Arabic (Morocco))",
                                        default=None, null=True)
    policy_uri_ar_om = fields.CharField(max_length=255, description="Policy URI (Arabic (Oman))", default=None,
                                        null=True)
    policy_uri_ar_qa = fields.CharField(max_length=255, description="Policy URI (Arabic (Qatar))",
                                        default=None, null=True)
    policy_uri_ar_sa = fields.CharField(max_length=255, description="Policy URI (Arabic (Saudi Arabia))",
                                        default=None, null=True)
    policy_uri_ar_sy = fields.CharField(max_length=255, description="Policy URI (Arabic (Syria))",
                                        default=None, null=True)
    policy_uri_ar_tn = fields.CharField(max_length=255, description="Policy URI (Arabic (Tunisia))",
                                        default=None, null=True)
    policy_uri_ar_ye = fields.CharField(max_length=255, description="Policy URI (Arabic (Yemen))",
                                        default=None, null=True)
    policy_uri_az_az = fields.CharField(max_length=255, description="Policy URI (Azeri (Latin) (Azerbaijan))",
                                        default=None, null=True)
    policy_uri_az_cyrl_az = fields.CharField(max_length=255,
                                             description="Policy URI (Azeri (Cyrillic) (Azerbaijan))",
                                             default=None, null=True)
    policy_uri_be_by = fields.CharField(max_length=255, description="Policy URI (Belarusian (Belarus))",
                                        default=None, null=True)
    policy_uri_bg_bg = fields.CharField(max_length=255, description="Policy URI (Bulgarian (Bulgaria))",
                                        default=None, null=True)
    policy_uri_bs_ba = fields.CharField(max_length=255,
                                        description="Policy URI (Bosnian (Bosnia and Herzegovina))", default=None,
                                        null=True)
    policy_uri_ca_es = fields.CharField(max_length=255, description="Policy URI (Catalan (Spain))",
                                        default=None, null=True)
    policy_uri_cs_cz = fields.CharField(max_length=255, description="Policy URI (Czech (Czech Republic))",
                                        default=None, null=True)
    policy_uri_cy_gb = fields.CharField(max_length=255, description="Policy URI (Welsh (United Kingdom))",
                                        default=None, null=True)
    policy_uri_da_dk = fields.CharField(max_length=255, description="Policy URI (Danish (Denmark))",
                                        default=None, null=True)
    policy_uri_de_at = fields.CharField(max_length=255, description="Policy URI (German (Austria))",
                                        default=None, null=True)
    policy_uri_de_ch = fields.CharField(max_length=255, description="Policy URI (German (Switzerland))",
                                        default=None, null=True)
    policy_uri_de_de = fields.CharField(max_length=255, description="Policy URI (German (Germany))",
                                        default=None, null=True)
    policy_uri_de_li = fields.CharField(max_length=255, description="Policy URI (German (Liechtenstein))",
                                        default=None, null=True)
    policy_uri_de_lu = fields.CharField(max_length=255, description="Policy URI (German (Luxembourg))",
                                        default=None, null=True)
    policy_uri_dv_mv = fields.CharField(max_length=255, description="Policy URI (Divehi (Maldives))",
                                        default=None, null=True)
    policy_uri_el_gr = fields.CharField(max_length=255, description="Policy URI (Greek (Greece))",
                                        default=None, null=True)
    policy_uri_en_au = fields.CharField(max_length=255, description="Policy URI (English (Australia))",
                                        default=None, null=True)
    policy_uri_en_bz = fields.CharField(max_length=255, description="Policy URI (English (Belize))",
                                        default=None, null=True)
    policy_uri_en_ca = fields.CharField(max_length=255, description="Policy URI (English (Canada))",
                                        default=None, null=True)
    policy_uri_en_cb = fields.CharField(max_length=255, description="Policy URI (English (Caribbean))",
                                        default=None, null=True)
    policy_uri_en_gb = fields.CharField(max_length=255, description="Policy URI (English (United Kingdom))",
                                        default=None, null=True)
    policy_uri_en_ie = fields.CharField(max_length=255, description="Policy URI (English (Ireland))",
                                        default=None, null=True)
    policy_uri_en_jm = fields.CharField(max_length=255, description="Policy URI (English (Jamaica))",
                                        default=None, null=True)
    policy_uri_en_nz = fields.CharField(max_length=255, description="Policy URI (English (New Zealand))",
                                        default=None, null=True)
    policy_uri_en_ph = fields.CharField(max_length=255,
                                        description="Policy URI (English (Republic of the Philippines))",
                                        default=None, null=True)
    policy_uri_en_tt = fields.CharField(max_length=255,
                                        description="Policy URI (English (Trinidad and Tobago))",
                                        default=None, null=True)
    policy_uri_en_us = fields.CharField(max_length=255, description="Policy URI (English (United States))",
                                        default=None, null=True)
    policy_uri_en_za = fields.CharField(max_length=255, description="Policy URI (English (South Africa))",
                                        default=None, null=True)
    policy_uri_en_zw = fields.CharField(max_length=255, description="Policy URI (English (Zimbabwe))",
                                        default=None, null=True)
    policy_uri_es_ar = fields.CharField(max_length=255, description="Policy URI (Spanish (Argentina))",
                                        default=None, null=True)
    policy_uri_es_bo = fields.CharField(max_length=255, description="Policy URI (Spanish (Bolivia))",
                                        default=None, null=True)
    policy_uri_es_cl = fields.CharField(max_length=255, description="Policy URI (Spanish (Chile))",
                                        default=None, null=True)
    policy_uri_es_co = fields.CharField(max_length=255, description="Policy URI (Spanish (Colombia))",
                                        default=None, null=True)
    policy_uri_es_cr = fields.CharField(max_length=255, description="Policy URI (Spanish (Costa Rica))",
                                        default=None, null=True)
    policy_uri_es_do = fields.CharField(max_length=255,
                                        description="Policy URI (Spanish (Dominican Republic))",
                                        default=None, null=True)
    policy_uri_es_ec = fields.CharField(max_length=255, description="Policy URI (Spanish (Ecuador))",
                                        default=None, null=True)
    policy_uri_es_es = fields.CharField(max_length=255, description="Policy URI (Spanish (Spain))",
                                        default=None, null=True)
    policy_uri_es_gt = fields.CharField(max_length=255, description="Policy URI (Spanish (Guatemala))",
                                        default=None, null=True)
    policy_uri_es_hn = fields.CharField(max_length=255, description="Policy URI (Spanish (Honduras))",
                                        default=None, null=True)
    policy_uri_es_mx = fields.CharField(max_length=255, description="Policy URI (Spanish (Mexico))",
                                        default=None, null=True)
    policy_uri_es_ni = fields.CharField(max_length=255, description="Policy URI (Spanish (Nicaragua))",
                                        default=None, null=True)
    policy_uri_es_pa = fields.CharField(max_length=255, description="Policy URI (Spanish (Panama))",
                                        default=None, null=True)
    policy_uri_es_pe = fields.CharField(max_length=255, description="Policy URI (Spanish (Peru))",
                                        default=None, null=True)
    policy_uri_es_pr = fields.CharField(max_length=255, description="Policy URI (Spanish (Puerto Rico))",
                                        default=None, null=True)
    policy_uri_es_py = fields.CharField(max_length=255, description="Policy URI (Spanish (Paraguay))",
                                        default=None, null=True)
    policy_uri_es_sv = fields.CharField(max_length=255, description="Policy URI (Spanish (El Salvador))",
                                        default=None, null=True)
    policy_uri_es_uy = fields.CharField(max_length=255, description="Policy URI (Spanish (Uruguay))",
                                        default=None, null=True)
    policy_uri_es_ve = fields.CharField(max_length=255, description="Policy URI (Spanish (Venezuela))",
                                        default=None, null=True)
    policy_uri_et_ee = fields.CharField(max_length=255, description="Policy URI (Estonian (Estonia))",
                                        default=None, null=True)
    policy_uri_eu_es = fields.CharField(max_length=255, description="Policy URI (Basque (Spain))",
                                        default=None, null=True)
    policy_uri_fa_ir = fields.CharField(max_length=255, description="Policy URI (Farsi (Iran))", default=None,
                                        null=True)
    policy_uri_fi_fi = fields.CharField(max_length=255, description="Policy URI (Finnish (Finland))",
                                        default=None, null=True)
    policy_uri_fo_fo = fields.CharField(max_length=255, description="Policy URI (Faroese (Faroe Islands))",
                                        default=None, null=True)
    policy_uri_fr_be = fields.CharField(max_length=255, description="Policy URI (French (Belgium))",
                                        default=None, null=True)
    policy_uri_fr_ca = fields.CharField(max_length=255, description="Policy URI (French (Canada))",
                                        default=None, null=True)
    policy_uri_fr_ch = fields.CharField(max_length=255, description="Policy URI (French (Switzerland))",
                                        default=None, null=True)
    policy_uri_fr_fr = fields.CharField(max_length=255, description="Policy URI (French (France))",
                                        default=None, null=True)
    policy_uri_fr_lu = fields.CharField(max_length=255, description="Policy URI (French (Luxembourg))",
                                        default=None, null=True)
    policy_uri_fr_mc = fields.CharField(max_length=255,
                                        description="Policy URI (French (Principality of Monaco))",
                                        default=None, null=True)
    policy_uri_gl_es = fields.CharField(max_length=255, description="Policy URI (Galician (Spain))",
                                        default=None, null=True)
    policy_uri_gu_in = fields.CharField(max_length=255, description="Policy URI (Gujarati (India))",
                                        default=None, null=True)
    policy_uri_he_il = fields.CharField(max_length=255, description="Policy URI (Hebrew (Israel))",
                                        default=None, null=True)
    policy_uri_hi_in = fields.CharField(max_length=255, description="Policy URI (Hindi (India))", default=None,
                                        null=True)
    policy_uri_hr_ba = fields.CharField(max_length=255,
                                        description="Policy URI (Croatian (Bosnia and Herzegovina))", default=None,
                                        null=True)
    policy_uri_hr_hr = fields.CharField(max_length=255, description="Policy URI (Croatian (Croatia))",
                                        default=None, null=True)
    policy_uri_hu_hu = fields.CharField(max_length=255, description="Policy URI (Hungarian (Hungary))",
                                        default=None, null=True)
    policy_uri_hy_am = fields.CharField(max_length=255, description="Policy URI (Armenian (Armenia))",
                                        default=None, null=True)
    policy_uri_id_id = fields.CharField(max_length=255, description="Policy URI (Indonesian (Indonesia))",
                                        default=None, null=True)
    policy_uri_is_is = fields.CharField(max_length=255, description="Policy URI (Icelandic (Iceland))",
                                        default=None, null=True)
    policy_uri_it_ch = fields.CharField(max_length=255, description="Policy URI (Italian (Switzerland))",
                                        default=None, null=True)
    policy_uri_it_it = fields.CharField(max_length=255, description="Policy URI (Italian (Italy))",
                                        default=None, null=True)
    policy_uri_ja_jp = fields.CharField(max_length=255, description="Policy URI (Japanese (Japan))",
                                        default=None, null=True)
    policy_uri_ka_ge = fields.CharField(max_length=255, description="Policy URI (Georgian (Georgia))",
                                        default=None, null=True)
    policy_uri_kk_kz = fields.CharField(max_length=255, description="Policy URI (Kazakh (Kazakhstan))",
                                        default=None, null=True)
    policy_uri_kn_in = fields.CharField(max_length=255, description="Policy URI (Kannada (India))",
                                        default=None, null=True)
    policy_uri_ko_kr = fields.CharField(max_length=255, description="Policy URI (Korean (Korea))",
                                        default=None, null=True)
    policy_uri_kok_in = fields.CharField(max_length=255, description="Policy URI (Konkani (India))",
                                         default=None, null=True)
    policy_uri_ky_kg = fields.CharField(max_length=255, description="Policy URI (Kyrgyz (Kyrgyzstan))",
                                        default=None, null=True)
    policy_uri_lt_lt = fields.CharField(max_length=255, description="Policy URI (Lithuanian (Lithuania))",
                                        default=None, null=True)
    policy_uri_lv_lv = fields.CharField(max_length=255, description="Policy URI (Latvian (Latvia))",
                                        default=None, null=True)
    policy_uri_mi_nz = fields.CharField(max_length=255, description="Policy URI (Maori (New Zealand))",
                                        default=None, null=True)
    policy_uri_mk_mk = fields.CharField(max_length=255,
                                        description="Policy URI (FYRO Macedonian (Former Yugoslav Republic of Macedonia))",
                                        default=None, null=True)
    policy_uri_mn_mn = fields.CharField(max_length=255, description="Policy URI (Mongolian (Mongolia))",
                                        default=None, null=True)
    policy_uri_mr_in = fields.CharField(max_length=255, description="Policy URI (Marathi (India))",
                                        default=None, null=True)
    policy_uri_ms_bn = fields.CharField(max_length=255, description="Policy URI (Malay (Brunei Darussalam))",
                                        default=None, null=True)
    policy_uri_ms_my = fields.CharField(max_length=255, description="Policy URI (Malay (Malaysia))",
                                        default=None, null=True)
    policy_uri_mt_mt = fields.CharField(max_length=255, description="Policy URI (Maltese (Malta))",
                                        default=None, null=True)
    policy_uri_nb_no = fields.CharField(max_length=255, description="Policy URI (Norwegian (Bokm?l) (Norway))",
                                        default=None, null=True)
    policy_uri_nl_be = fields.CharField(max_length=255, description="Policy URI (Dutch (Belgium))",
                                        default=None, null=True)
    policy_uri_nl_nl = fields.CharField(max_length=255, description="Policy URI (Dutch (Netherlands))",
                                        default=None, null=True)
    policy_uri_nn_no = fields.CharField(max_length=255,
                                        description="Policy URI (Norwegian (Nynorsk) (Norway))",
                                        default=None, null=True)
    policy_uri_ns_za = fields.CharField(max_length=255,
                                        description="Policy URI (Northern Sotho (South Africa))",
                                        default=None, null=True)
    policy_uri_pa_in = fields.CharField(max_length=255, description="Policy URI (Punjabi (India))",
                                        default=None, null=True)
    policy_uri_pl_pl = fields.CharField(max_length=255, description="Policy URI (Polish (Poland))",
                                        default=None, null=True)
    policy_uri_ps_ar = fields.CharField(max_length=255, description="Policy URI (Pashto (Afghanistan))",
                                        default=None, null=True)
    policy_uri_pt_br = fields.CharField(max_length=255, description="Policy URI (Portuguese (Brazil))",
                                        default=None, null=True)
    policy_uri_pt_pt = fields.CharField(max_length=255, description="Policy URI (Portuguese (Portugal))",
                                        default=None, null=True)
    policy_uri_qu_bo = fields.CharField(max_length=255, description="Policy URI (Quechua (Bolivia))",
                                        default=None, null=True)
    policy_uri_qu_ec = fields.CharField(max_length=255, description="Policy URI (Quechua (Ecuador))",
                                        default=None, null=True)
    policy_uri_qu_pe = fields.CharField(max_length=255, description="Policy URI (Quechua (Peru))",
                                        default=None, null=True)
    policy_uri_ro_ro = fields.CharField(max_length=255, description="Policy URI (Romanian (Romania))",
                                        default=None, null=True)
    policy_uri_ru_ru = fields.CharField(max_length=255, description="Policy URI (Russian (Russia))",
                                        default=None, null=True)
    policy_uri_sa_in = fields.CharField(max_length=255, description="Policy URI (Sanskrit (India))",
                                        default=None, null=True)
    policy_uri_se_fi = fields.CharField(max_length=255, description="Policy URI (Sami (Finland))",
                                        default=None, null=True)
    policy_uri_se_no = fields.CharField(max_length=255, description="Policy URI (Sami (Norway))", default=None,
                                        null=True)
    policy_uri_se_se = fields.CharField(max_length=255, description="Policy URI (Sami (Sweden))", default=None,
                                        null=True)
    policy_uri_sk_sk = fields.CharField(max_length=255, description="Policy URI (Slovak (Slovakia))",
                                        default=None, null=True)
    policy_uri_sl_si = fields.CharField(max_length=255, description="Policy URI (Slovenian (Slovenia))",
                                        default=None, null=True)
    policy_uri_sq_al = fields.CharField(max_length=255, description="Policy URI (Albanian (Albania))",
                                        default=None, null=True)
    policy_uri_sr_ba = fields.CharField(max_length=255,
                                        description="Policy URI (Serbian (Latin) (Bosnia and Herzegovina))",
                                        default=None, null=True)
    policy_uri_sr_cyrl_ba = fields.CharField(max_length=255,
                                             description="Policy URI (Serbian (Cyrillic) (Bosnia and Herzegovina))",
                                             default=None, null=True)
    policy_uri_sr_sp = fields.CharField(max_length=255,
                                        description="Policy URI (Serbian (Latin) (Serbia and Montenegro))",
                                        default=None, null=True)
    policy_uri_sr_cyrl_sp = fields.CharField(max_length=255,
                                             description="Policy URI (Serbian (Cyrillic) (Serbia and Montenegro))",
                                             default=None, null=True)
    policy_uri_sv_fi = fields.CharField(max_length=255, description="Policy URI (Swedish (Finland))",
                                        default=None, null=True)
    policy_uri_sv_se = fields.CharField(max_length=255, description="Policy URI (Swedish (Sweden))",
                                        default=None, null=True)
    policy_uri_sw_ke = fields.CharField(max_length=255, description="Policy URI (Swahili (Kenya))",
                                        default=None, null=True)
    policy_uri_syr_sy = fields.CharField(max_length=255, description="Policy URI (Syriac (Syria))",
                                         default=None, null=True)
    policy_uri_ta_in = fields.CharField(max_length=255, description="Policy URI (Tamil (India))", default=None,
                                        null=True)
    policy_uri_te_in = fields.CharField(max_length=255, description="Policy URI (Telugu (India))",
                                        default=None, null=True)
    policy_uri_th_th = fields.CharField(max_length=255, description="Policy URI (Thai (Thailand))",
                                        default=None, null=True)
    policy_uri_tl_ph = fields.CharField(max_length=255, description="Policy URI (Tagalog (Philippines))",
                                        default=None, null=True)
    policy_uri_tn_za = fields.CharField(max_length=255, description="Policy URI (Tswana (South Africa))",
                                        default=None, null=True)
    policy_uri_tr_tr = fields.CharField(max_length=255, description="Policy URI (Turkish (Turkey))",
                                        default=None, null=True)
    policy_uri_tt_ru = fields.CharField(max_length=255, description="Policy URI (Tatar (Russia))",
                                        default=None, null=True)
    policy_uri_uk_ua = fields.CharField(max_length=255, description="Policy URI (Ukrainian (Ukraine))",
                                        default=None, null=True)
    policy_uri_ur_pk = fields.CharField(max_length=255,
                                        description="Policy URI (Urdu (Islamic Republic of Pakistan))",
                                        default=None, null=True)
    policy_uri_uz_uz = fields.CharField(max_length=255, description="Policy URI (Uzbek (Latin) (Uzbekistan))",
                                        default=None, null=True)
    policy_uri_uz_cyrl_uz = fields.CharField(max_length=255,
                                             description="Policy URI (Uzbek (Cyrillic) (Uzbekistan))",
                                             default=None, null=True)
    policy_uri_vi_vn = fields.CharField(max_length=255, description="Policy URI (Vietnamese (Viet Nam))",
                                        default=None, null=True)
    policy_uri_xh_za = fields.CharField(max_length=255, description="Policy URI (Xhosa (South Africa))",
                                        default=None, null=True)
    policy_uri_zh_cn = fields.CharField(max_length=255, description="Policy URI (Chinese (S))", default=None,
                                        null=True)
    policy_uri_zh_hk = fields.CharField(max_length=255, description="Policy URI (Chinese (Hong Kong))",
                                        default=None, null=True)
    policy_uri_zh_mo = fields.CharField(max_length=255, description="Policy URI (Chinese (Macau))",
                                        default=None, null=True)
    policy_uri_zh_sg = fields.CharField(max_length=255, description="Policy URI (Chinese (Singapore))",
                                        default=None, null=True)
    policy_uri_zh_tw = fields.CharField(max_length=255, description="Policy URI (Chinese (T))", default=None,
                                        null=True)
    policy_uri_zu_za = fields.CharField(max_length=255, description="Policy URI (Zulu (South Africa))",
                                        default=None, null=True)


class LogoURI(Model):
    client: fields.ForeignKeyRelation[Clients] = fields.ForeignKeyField('main.Clients', 'logo_uris', pk=True)
    logo_uri = fields.CharField(max_length=255,
                                description="URL string that references a logo for the client.",
                                default=None, null=True)

    logo_uri_af_za = fields.CharField(max_length=255, description="Logo URI (Afrikaans (South Africa))",
                                      default=None, null=True)
    logo_uri_ar_ae = fields.CharField(max_length=255, description="Logo URI (Arabic (U.A.E.))", default=None,
                                      null=True)
    logo_uri_ar_bh = fields.CharField(max_length=255, description="Logo URI (Arabic (Bahrain))", default=None,
                                      null=True)
    logo_uri_ar_dz = fields.CharField(max_length=255, description="Logo URI (Arabic (Algeria))", default=None,
                                      null=True)
    logo_uri_ar_eg = fields.CharField(max_length=255, description="Logo URI (Arabic (Egypt))", default=None,
                                      null=True)
    logo_uri_ar_iq = fields.CharField(max_length=255, description="Logo URI (Arabic (Iraq))", default=None,
                                      null=True)
    logo_uri_ar_jo = fields.CharField(max_length=255, description="Logo URI (Arabic (Jordan))", default=None,
                                      null=True)
    logo_uri_ar_kw = fields.CharField(max_length=255, description="Logo URI (Arabic (Kuwait))", default=None,
                                      null=True)
    logo_uri_ar_lb = fields.CharField(max_length=255, description="Logo URI (Arabic (Lebanon))", default=None,
                                      null=True)
    logo_uri_ar_ly = fields.CharField(max_length=255, description="Logo URI (Arabic (Libya))", default=None,
                                      null=True)
    logo_uri_ar_ma = fields.CharField(max_length=255, description="Logo URI (Arabic (Morocco))", default=None,
                                      null=True)
    logo_uri_ar_om = fields.CharField(max_length=255, description="Logo URI (Arabic (Oman))", default=None,
                                      null=True)
    logo_uri_ar_qa = fields.CharField(max_length=255, description="Logo URI (Arabic (Qatar))", default=None,
                                      null=True)
    logo_uri_ar_sa = fields.CharField(max_length=255, description="Logo URI (Arabic (Saudi Arabia))",
                                      default=None, null=True)
    logo_uri_ar_sy = fields.CharField(max_length=255, description="Logo URI (Arabic (Syria))", default=None,
                                      null=True)
    logo_uri_ar_tn = fields.CharField(max_length=255, description="Logo URI (Arabic (Tunisia))", default=None,
                                      null=True)
    logo_uri_ar_ye = fields.CharField(max_length=255, description="Logo URI (Arabic (Yemen))", default=None,
                                      null=True)
    logo_uri_az_az = fields.CharField(max_length=255, description="Logo URI (Azeri (Latin) (Azerbaijan))",
                                      default=None, null=True)
    logo_uri_az_cyrl_az = fields.CharField(max_length=255,
                                           description="Logo URI (Azeri (Cyrillic) (Azerbaijan))", default=None,
                                           null=True)
    logo_uri_be_by = fields.CharField(max_length=255, description="Logo URI (Belarusian (Belarus))",
                                      default=None, null=True)
    logo_uri_bg_bg = fields.CharField(max_length=255, description="Logo URI (Bulgarian (Bulgaria))",
                                      default=None, null=True)
    logo_uri_bs_ba = fields.CharField(max_length=255, description="Logo URI (Bosnian (Bosnia and Herzegovina))",
                                      default=None, null=True)
    logo_uri_ca_es = fields.CharField(max_length=255, description="Logo URI (Catalan (Spain))", default=None,
                                      null=True)
    logo_uri_cs_cz = fields.CharField(max_length=255, description="Logo URI (Czech (Czech Republic))",
                                      default=None, null=True)
    logo_uri_cy_gb = fields.CharField(max_length=255, description="Logo URI (Welsh (United Kingdom))",
                                      default=None, null=True)
    logo_uri_da_dk = fields.CharField(max_length=255, description="Logo URI (Danish (Denmark))", default=None,
                                      null=True)
    logo_uri_de_at = fields.CharField(max_length=255, description="Logo URI (German (Austria))", default=None,
                                      null=True)
    logo_uri_de_ch = fields.CharField(max_length=255, description="Logo URI (German (Switzerland))",
                                      default=None, null=True)
    logo_uri_de_de = fields.CharField(max_length=255, description="Logo URI (German (Germany))", default=None,
                                      null=True)
    logo_uri_de_li = fields.CharField(max_length=255, description="Logo URI (German (Liechtenstein))",
                                      default=None, null=True)
    logo_uri_de_lu = fields.CharField(max_length=255, description="Logo URI (German (Luxembourg))", default=None,
                                      null=True)
    logo_uri_dv_mv = fields.CharField(max_length=255, description="Logo URI (Divehi (Maldives))", default=None,
                                      null=True)
    logo_uri_el_gr = fields.CharField(max_length=255, description="Logo URI (Greek (Greece))", default=None,
                                      null=True)
    logo_uri_en_au = fields.CharField(max_length=255, description="Logo URI (English (Australia))", default=None,
                                      null=True)
    logo_uri_en_bz = fields.CharField(max_length=255, description="Logo URI (English (Belize))", default=None,
                                      null=True)
    logo_uri_en_ca = fields.CharField(max_length=255, description="Logo URI (English (Canada))", default=None,
                                      null=True)
    logo_uri_en_cb = fields.CharField(max_length=255, description="Logo URI (English (Caribbean))", default=None,
                                      null=True)
    logo_uri_en_gb = fields.CharField(max_length=255, description="Logo URI (English (United Kingdom))",
                                      default=None, null=True)
    logo_uri_en_ie = fields.CharField(max_length=255, description="Logo URI (English (Ireland))", default=None,
                                      null=True)
    logo_uri_en_jm = fields.CharField(max_length=255, description="Logo URI (English (Jamaica))", default=None,
                                      null=True)
    logo_uri_en_nz = fields.CharField(max_length=255, description="Logo URI (English (New Zealand))",
                                      default=None, null=True)
    logo_uri_en_ph = fields.CharField(max_length=255,
                                      description="Logo URI (English (Republic of the Philippines))",
                                      default=None, null=True)
    logo_uri_en_tt = fields.CharField(max_length=255, description="Logo URI (English (Trinidad and Tobago))",
                                      default=None, null=True)
    logo_uri_en_us = fields.CharField(max_length=255, description="Logo URI (English (United States))",
                                      default=None, null=True)
    logo_uri_en_za = fields.CharField(max_length=255, description="Logo URI (English (South Africa))",
                                      default=None, null=True)
    logo_uri_en_zw = fields.CharField(max_length=255, description="Logo URI (English (Zimbabwe))", default=None,
                                      null=True)
    logo_uri_es_ar = fields.CharField(max_length=255, description="Logo URI (Spanish (Argentina))", default=None,
                                      null=True)
    logo_uri_es_bo = fields.CharField(max_length=255, description="Logo URI (Spanish (Bolivia))", default=None,
                                      null=True)
    logo_uri_es_cl = fields.CharField(max_length=255, description="Logo URI (Spanish (Chile))", default=None,
                                      null=True)
    logo_uri_es_co = fields.CharField(max_length=255, description="Logo URI (Spanish (Colombia))", default=None,
                                      null=True)
    logo_uri_es_cr = fields.CharField(max_length=255, description="Logo URI (Spanish (Costa Rica))",
                                      default=None, null=True)
    logo_uri_es_do = fields.CharField(max_length=255, description="Logo URI (Spanish (Dominican Republic))",
                                      default=None, null=True)
    logo_uri_es_ec = fields.CharField(max_length=255, description="Logo URI (Spanish (Ecuador))", default=None,
                                      null=True)
    logo_uri_es_es = fields.CharField(max_length=255, description="Logo URI (Spanish (Spain))", default=None,
                                      null=True)
    logo_uri_es_gt = fields.CharField(max_length=255, description="Logo URI (Spanish (Guatemala))", default=None,
                                      null=True)
    logo_uri_es_hn = fields.CharField(max_length=255, description="Logo URI (Spanish (Honduras))", default=None,
                                      null=True)
    logo_uri_es_mx = fields.CharField(max_length=255, description="Logo URI (Spanish (Mexico))", default=None,
                                      null=True)
    logo_uri_es_ni = fields.CharField(max_length=255, description="Logo URI (Spanish (Nicaragua))", default=None,
                                      null=True)
    logo_uri_es_pa = fields.CharField(max_length=255, description="Logo URI (Spanish (Panama))", default=None,
                                      null=True)
    logo_uri_es_pe = fields.CharField(max_length=255, description="Logo URI (Spanish (Peru))", default=None,
                                      null=True)
    logo_uri_es_pr = fields.CharField(max_length=255, description="Logo URI (Spanish (Puerto Rico))",
                                      default=None, null=True)
    logo_uri_es_py = fields.CharField(max_length=255, description="Logo URI (Spanish (Paraguay))", default=None,
                                      null=True)
    logo_uri_es_sv = fields.CharField(max_length=255, description="Logo URI (Spanish (El Salvador))",
                                      default=None, null=True)
    logo_uri_es_uy = fields.CharField(max_length=255, description="Logo URI (Spanish (Uruguay))", default=None,
                                      null=True)
    logo_uri_es_ve = fields.CharField(max_length=255, description="Logo URI (Spanish (Venezuela))", default=None,
                                      null=True)
    logo_uri_et_ee = fields.CharField(max_length=255, description="Logo URI (Estonian (Estonia))", default=None,
                                      null=True)
    logo_uri_eu_es = fields.CharField(max_length=255, description="Logo URI (Basque (Spain))", default=None,
                                      null=True)
    logo_uri_fa_ir = fields.CharField(max_length=255, description="Logo URI (Farsi (Iran))", default=None,
                                      null=True)
    logo_uri_fi_fi = fields.CharField(max_length=255, description="Logo URI (Finnish (Finland))", default=None,
                                      null=True)
    logo_uri_fo_fo = fields.CharField(max_length=255, description="Logo URI (Faroese (Faroe Islands))",
                                      default=None, null=True)
    logo_uri_fr_be = fields.CharField(max_length=255, description="Logo URI (French (Belgium))", default=None,
                                      null=True)
    logo_uri_fr_ca = fields.CharField(max_length=255, description="Logo URI (French (Canada))", default=None,
                                      null=True)
    logo_uri_fr_ch = fields.CharField(max_length=255, description="Logo URI (French (Switzerland))",
                                      default=None, null=True)
    logo_uri_fr_fr = fields.CharField(max_length=255, description="Logo URI (French (France))", default=None,
                                      null=True)
    logo_uri_fr_lu = fields.CharField(max_length=255, description="Logo URI (French (Luxembourg))", default=None,
                                      null=True)
    logo_uri_fr_mc = fields.CharField(max_length=255, description="Logo URI (French (Principality of Monaco))",
                                      default=None, null=True)
    logo_uri_gl_es = fields.CharField(max_length=255, description="Logo URI (Galician (Spain))", default=None,
                                      null=True)
    logo_uri_gu_in = fields.CharField(max_length=255, description="Logo URI (Gujarati (India))", default=None,
                                      null=True)
    logo_uri_he_il = fields.CharField(max_length=255, description="Logo URI (Hebrew (Israel))", default=None,
                                      null=True)
    logo_uri_hi_in = fields.CharField(max_length=255, description="Logo URI (Hindi (India))", default=None,
                                      null=True)
    logo_uri_hr_ba = fields.CharField(max_length=255, description="Logo URI (Croatian (Bosnia and Herzegovina))",
                                      default=None, null=True)
    logo_uri_hr_hr = fields.CharField(max_length=255, description="Logo URI (Croatian (Croatia))", default=None,
                                      null=True)
    logo_uri_hu_hu = fields.CharField(max_length=255, description="Logo URI (Hungarian (Hungary))", default=None,
                                      null=True)
    logo_uri_hy_am = fields.CharField(max_length=255, description="Logo URI (Armenian (Armenia))", default=None,
                                      null=True)
    logo_uri_id_id = fields.CharField(max_length=255, description="Logo URI (Indonesian (Indonesia))",
                                      default=None, null=True)
    logo_uri_is_is = fields.CharField(max_length=255, description="Logo URI (Icelandic (Iceland))", default=None,
                                      null=True)
    logo_uri_it_ch = fields.CharField(max_length=255, description="Logo URI (Italian (Switzerland))",
                                      default=None, null=True)
    logo_uri_it_it = fields.CharField(max_length=255, description="Logo URI (Italian (Italy))", default=None,
                                      null=True)
    logo_uri_ja_jp = fields.CharField(max_length=255, description="Logo URI (Japanese (Japan))", default=None,
                                      null=True)
    logo_uri_ka_ge = fields.CharField(max_length=255, description="Logo URI (Georgian (Georgia))", default=None,
                                      null=True)
    logo_uri_kk_kz = fields.CharField(max_length=255, description="Logo URI (Kazakh (Kazakhstan))", default=None,
                                      null=True)
    logo_uri_kn_in = fields.CharField(max_length=255, description="Logo URI (Kannada (India))", default=None,
                                      null=True)
    logo_uri_ko_kr = fields.CharField(max_length=255, description="Logo URI (Korean (Korea))", default=None,
                                      null=True)
    logo_uri_kok_in = fields.CharField(max_length=255, description="Logo URI (Konkani (India))", default=None,
                                       null=True)
    logo_uri_ky_kg = fields.CharField(max_length=255, description="Logo URI (Kyrgyz (Kyrgyzstan))", default=None,
                                      null=True)
    logo_uri_lt_lt = fields.CharField(max_length=255, description="Logo URI (Lithuanian (Lithuania))",
                                      default=None, null=True)
    logo_uri_lv_lv = fields.CharField(max_length=255, description="Logo URI (Latvian (Latvia))", default=None,
                                      null=True)
    logo_uri_mi_nz = fields.CharField(max_length=255, description="Logo URI (Maori (New Zealand))", default=None,
                                      null=True)
    logo_uri_mk_mk = fields.CharField(max_length=255,
                                      description="Logo URI (FYRO Macedonian (Former Yugoslav Republic of Macedonia))",
                                      default=None, null=True)
    logo_uri_mn_mn = fields.CharField(max_length=255, description="Logo URI (Mongolian (Mongolia))",
                                      default=None, null=True)
    logo_uri_mr_in = fields.CharField(max_length=255, description="Logo URI (Marathi (India))", default=None,
                                      null=True)
    logo_uri_ms_bn = fields.CharField(max_length=255, description="Logo URI (Malay (Brunei Darussalam))",
                                      default=None, null=True)
    logo_uri_ms_my = fields.CharField(max_length=255, description="Logo URI (Malay (Malaysia))", default=None,
                                      null=True)
    logo_uri_mt_mt = fields.CharField(max_length=255, description="Logo URI (Maltese (Malta))", default=None,
                                      null=True)
    logo_uri_nb_no = fields.CharField(max_length=255, description="Logo URI (Norwegian (Bokm?l) (Norway))",
                                      default=None, null=True)
    logo_uri_nl_be = fields.CharField(max_length=255, description="Logo URI (Dutch (Belgium))", default=None,
                                      null=True)
    logo_uri_nl_nl = fields.CharField(max_length=255, description="Logo URI (Dutch (Netherlands))", default=None,
                                      null=True)
    logo_uri_nn_no = fields.CharField(max_length=255, description="Logo URI (Norwegian (Nynorsk) (Norway))",
                                      default=None, null=True)
    logo_uri_ns_za = fields.CharField(max_length=255, description="Logo URI (Northern Sotho (South Africa))",
                                      default=None, null=True)
    logo_uri_pa_in = fields.CharField(max_length=255, description="Logo URI (Punjabi (India))", default=None,
                                      null=True)
    logo_uri_pl_pl = fields.CharField(max_length=255, description="Logo URI (Polish (Poland))", default=None,
                                      null=True)
    logo_uri_ps_ar = fields.CharField(max_length=255, description="Logo URI (Pashto (Afghanistan))",
                                      default=None, null=True)
    logo_uri_pt_br = fields.CharField(max_length=255, description="Logo URI (Portuguese (Brazil))", default=None,
                                      null=True)
    logo_uri_pt_pt = fields.CharField(max_length=255, description="Logo URI (Portuguese (Portugal))",
                                      default=None, null=True)
    logo_uri_qu_bo = fields.CharField(max_length=255, description="Logo URI (Quechua (Bolivia))", default=None,
                                      null=True)
    logo_uri_qu_ec = fields.CharField(max_length=255, description="Logo URI (Quechua (Ecuador))", default=None,
                                      null=True)
    logo_uri_qu_pe = fields.CharField(max_length=255, description="Logo URI (Quechua (Peru))", default=None,
                                      null=True)
    logo_uri_ro_ro = fields.CharField(max_length=255, description="Logo URI (Romanian (Romania))", default=None,
                                      null=True)
    logo_uri_ru_ru = fields.CharField(max_length=255, description="Logo URI (Russian (Russia))", default=None,
                                      null=True)
    logo_uri_sa_in = fields.CharField(max_length=255, description="Logo URI (Sanskrit (India))", default=None,
                                      null=True)
    logo_uri_se_fi = fields.CharField(max_length=255, description="Logo URI (Sami (Finland))", default=None,
                                      null=True)
    logo_uri_se_no = fields.CharField(max_length=255, description="Logo URI (Sami (Norway))", default=None,
                                      null=True)
    logo_uri_se_se = fields.CharField(max_length=255, description="Logo URI (Sami (Sweden))", default=None,
                                      null=True)
    logo_uri_sk_sk = fields.CharField(max_length=255, description="Logo URI (Slovak (Slovakia))", default=None,
                                      null=True)
    logo_uri_sl_si = fields.CharField(max_length=255, description="Logo URI (Slovenian (Slovenia))",
                                      default=None, null=True)
    logo_uri_sq_al = fields.CharField(max_length=255, description="Logo URI (Albanian (Albania))", default=None,
                                      null=True)
    logo_uri_sr_ba = fields.CharField(max_length=255,
                                      description="Logo URI (Serbian (Latin) (Bosnia and Herzegovina))",
                                      default=None, null=True)
    logo_uri_sr_cyrl_ba = fields.CharField(max_length=255,
                                           description="Logo URI (Serbian (Cyrillic) (Bosnia and Herzegovina))",
                                           default=None, null=True)
    logo_uri_sr_sp = fields.CharField(max_length=255,
                                      description="Logo URI (Serbian (Latin) (Serbia and Montenegro))",
                                      default=None, null=True)
    logo_uri_sr_cyrl_sp = fields.CharField(max_length=255,
                                           description="Logo URI (Serbian (Cyrillic) (Serbia and Montenegro))",
                                           default=None, null=True)
    logo_uri_sv_fi = fields.CharField(max_length=255, description="Logo URI (Swedish (Finland))", default=None,
                                      null=True)
    logo_uri_sv_se = fields.CharField(max_length=255, description="Logo URI (Swedish (Sweden))", default=None,
                                      null=True)
    logo_uri_sw_ke = fields.CharField(max_length=255, description="Logo URI (Swahili (Kenya))", default=None,
                                      null=True)
    logo_uri_syr_sy = fields.CharField(max_length=255, description="Logo URI (Syriac (Syria))", default=None,
                                       null=True)
    logo_uri_ta_in = fields.CharField(max_length=255, description="Logo URI (Tamil (India))", default=None,
                                      null=True)
    logo_uri_te_in = fields.CharField(max_length=255, description="Logo URI (Telugu (India))", default=None,
                                      null=True)
    logo_uri_th_th = fields.CharField(max_length=255, description="Logo URI (Thai (Thailand))", default=None,
                                      null=True)
    logo_uri_tl_ph = fields.CharField(max_length=255, description="Logo URI (Tagalog (Philippines))",
                                      default=None, null=True)
    logo_uri_tn_za = fields.CharField(max_length=255, description="Logo URI (Tswana (South Africa))",
                                      default=None, null=True)
    logo_uri_tr_tr = fields.CharField(max_length=255, description="Logo URI (Turkish (Turkey))", default=None,
                                      null=True)
    logo_uri_tt_ru = fields.CharField(max_length=255, description="Logo URI (Tatar (Russia))", default=None,
                                      null=True)
    logo_uri_uk_ua = fields.CharField(max_length=255, description="Logo URI (Ukrainian (Ukraine))", default=None,
                                      null=True)
    logo_uri_ur_pk = fields.CharField(max_length=255,
                                      description="Logo URI (Urdu (Islamic Republic of Pakistan))",
                                      default=None, null=True)
    logo_uri_uz_uz = fields.CharField(max_length=255, description="Logo URI (Uzbek (Latin) (Uzbekistan))",
                                      default=None, null=True)
    logo_uri_uz_cyrl_uz = fields.CharField(max_length=255,
                                           description="Logo URI (Uzbek (Cyrillic) (Uzbekistan))", default=None,
                                           null=True)
    logo_uri_vi_vn = fields.CharField(max_length=255, description="Logo URI (Vietnamese (Viet Nam))",
                                      default=None, null=True)
    logo_uri_xh_za = fields.CharField(max_length=255, description="Logo URI (Xhosa (South Africa))",
                                      default=None, null=True)
    logo_uri_zh_cn = fields.CharField(max_length=255, description="Logo URI (Chinese (S))", default=None,
                                      null=True)
    logo_uri_zh_hk = fields.CharField(max_length=255, description="Logo URI (Chinese (Hong Kong))", default=None,
                                      null=True)
    logo_uri_zh_mo = fields.CharField(max_length=255, description="Logo URI (Chinese (Macau))", default=None,
                                      null=True)
    logo_uri_zh_sg = fields.CharField(max_length=255, description="Logo URI (Chinese (Singapore))", default=None,
                                      null=True)
    logo_uri_zh_tw = fields.CharField(max_length=255, description="Logo URI (Chinese (T))", default=None,
                                      null=True)
    logo_uri_zu_za = fields.CharField(max_length=255, description="Logo URI (Zulu (South Africa))", default=None,
                                      null=True)


class ClientURI(Model):
    client: fields.ForeignKeyRelation[Clients] = fields.ForeignKeyField('main.Clients', 'client_uris', pk=True)
    client_uri = fields.CharField(max_length=255,
                                  description="URL string of a web page providing information about the client.",
                                  default=None, null=True)

    client_uri_af_za = fields.CharField(max_length=255, description="Client URI (Afrikaans (South Africa))",
                                        default=None, null=True)
    client_uri_ar_ae = fields.CharField(max_length=255, description="Client URI (Arabic (U.A.E.))",
                                        default=None, null=True)
    client_uri_ar_bh = fields.CharField(max_length=255, description="Client URI (Arabic (Bahrain))",
                                        default=None, null=True)
    client_uri_ar_dz = fields.CharField(max_length=255, description="Client URI (Arabic (Algeria))",
                                        default=None, null=True)
    client_uri_ar_eg = fields.CharField(max_length=255, description="Client URI (Arabic (Egypt))",
                                        default=None, null=True)
    client_uri_ar_iq = fields.CharField(max_length=255, description="Client URI (Arabic (Iraq))", default=None,
                                        null=True)
    client_uri_ar_jo = fields.CharField(max_length=255, description="Client URI (Arabic (Jordan))",
                                        default=None, null=True)
    client_uri_ar_kw = fields.CharField(max_length=255, description="Client URI (Arabic (Kuwait))",
                                        default=None, null=True)
    client_uri_ar_lb = fields.CharField(max_length=255, description="Client URI (Arabic (Lebanon))",
                                        default=None, null=True)
    client_uri_ar_ly = fields.CharField(max_length=255, description="Client URI (Arabic (Libya))",
                                        default=None, null=True)
    client_uri_ar_ma = fields.CharField(max_length=255, description="Client URI (Arabic (Morocco))",
                                        default=None, null=True)
    client_uri_ar_om = fields.CharField(max_length=255, description="Client URI (Arabic (Oman))", default=None,
                                        null=True)
    client_uri_ar_qa = fields.CharField(max_length=255, description="Client URI (Arabic (Qatar))",
                                        default=None, null=True)
    client_uri_ar_sa = fields.CharField(max_length=255, description="Client URI (Arabic (Saudi Arabia))",
                                        default=None, null=True)
    client_uri_ar_sy = fields.CharField(max_length=255, description="Client URI (Arabic (Syria))",
                                        default=None, null=True)
    client_uri_ar_tn = fields.CharField(max_length=255, description="Client URI (Arabic (Tunisia))",
                                        default=None, null=True)
    client_uri_ar_ye = fields.CharField(max_length=255, description="Client URI (Arabic (Yemen))",
                                        default=None, null=True)
    client_uri_az_az = fields.CharField(max_length=255, description="Client URI (Azeri (Latin) (Azerbaijan))",
                                        default=None, null=True)
    client_uri_az_cyrl_az = fields.CharField(max_length=255,
                                             description="Client URI (Azeri (Cyrillic) (Azerbaijan))",
                                             default=None, null=True)
    client_uri_be_by = fields.CharField(max_length=255, description="Client URI (Belarusian (Belarus))",
                                        default=None, null=True)
    client_uri_bg_bg = fields.CharField(max_length=255, description="Client URI (Bulgarian (Bulgaria))",
                                        default=None, null=True)
    client_uri_bs_ba = fields.CharField(max_length=255,
                                        description="Client URI (Bosnian (Bosnia and Herzegovina))", default=None,
                                        null=True)
    client_uri_ca_es = fields.CharField(max_length=255, description="Client URI (Catalan (Spain))",
                                        default=None, null=True)
    client_uri_cs_cz = fields.CharField(max_length=255, description="Client URI (Czech (Czech Republic))",
                                        default=None, null=True)
    client_uri_cy_gb = fields.CharField(max_length=255, description="Client URI (Welsh (United Kingdom))",
                                        default=None, null=True)
    client_uri_da_dk = fields.CharField(max_length=255, description="Client URI (Danish (Denmark))",
                                        default=None, null=True)
    client_uri_de_at = fields.CharField(max_length=255, description="Client URI (German (Austria))",
                                        default=None, null=True)
    client_uri_de_ch = fields.CharField(max_length=255, description="Client URI (German (Switzerland))",
                                        default=None, null=True)
    client_uri_de_de = fields.CharField(max_length=255, description="Client URI (German (Germany))",
                                        default=None, null=True)
    client_uri_de_li = fields.CharField(max_length=255, description="Client URI (German (Liechtenstein))",
                                        default=None, null=True)
    client_uri_de_lu = fields.CharField(max_length=255, description="Client URI (German (Luxembourg))",
                                        default=None, null=True)
    client_uri_dv_mv = fields.CharField(max_length=255, description="Client URI (Divehi (Maldives))",
                                        default=None, null=True)
    client_uri_el_gr = fields.CharField(max_length=255, description="Client URI (Greek (Greece))",
                                        default=None, null=True)
    client_uri_en_au = fields.CharField(max_length=255, description="Client URI (English (Australia))",
                                        default=None, null=True)
    client_uri_en_bz = fields.CharField(max_length=255, description="Client URI (English (Belize))",
                                        default=None, null=True)
    client_uri_en_ca = fields.CharField(max_length=255, description="Client URI (English (Canada))",
                                        default=None, null=True)
    client_uri_en_cb = fields.CharField(max_length=255, description="Client URI (English (Caribbean))",
                                        default=None, null=True)
    client_uri_en_gb = fields.CharField(max_length=255, description="Client URI (English (United Kingdom))",
                                        default=None, null=True)
    client_uri_en_ie = fields.CharField(max_length=255, description="Client URI (English (Ireland))",
                                        default=None, null=True)
    client_uri_en_jm = fields.CharField(max_length=255, description="Client URI (English (Jamaica))",
                                        default=None, null=True)
    client_uri_en_nz = fields.CharField(max_length=255, description="Client URI (English (New Zealand))",
                                        default=None, null=True)
    client_uri_en_ph = fields.CharField(max_length=255,
                                        description="Client URI (English (Republic of the Philippines))",
                                        default=None, null=True)
    client_uri_en_tt = fields.CharField(max_length=255,
                                        description="Client URI (English (Trinidad and Tobago))",
                                        default=None, null=True)
    client_uri_en_us = fields.CharField(max_length=255, description="Client URI (English (United States))",
                                        default=None, null=True)
    client_uri_en_za = fields.CharField(max_length=255, description="Client URI (English (South Africa))",
                                        default=None, null=True)
    client_uri_en_zw = fields.CharField(max_length=255, description="Client URI (English (Zimbabwe))",
                                        default=None, null=True)
    client_uri_es_ar = fields.CharField(max_length=255, description="Client URI (Spanish (Argentina))",
                                        default=None, null=True)
    client_uri_es_bo = fields.CharField(max_length=255, description="Client URI (Spanish (Bolivia))",
                                        default=None, null=True)
    client_uri_es_cl = fields.CharField(max_length=255, description="Client URI (Spanish (Chile))",
                                        default=None, null=True)
    client_uri_es_co = fields.CharField(max_length=255, description="Client URI (Spanish (Colombia))",
                                        default=None, null=True)
    client_uri_es_cr = fields.CharField(max_length=255, description="Client URI (Spanish (Costa Rica))",
                                        default=None, null=True)
    client_uri_es_do = fields.CharField(max_length=255,
                                        description="Client URI (Spanish (Dominican Republic))",
                                        default=None, null=True)
    client_uri_es_ec = fields.CharField(max_length=255, description="Client URI (Spanish (Ecuador))",
                                        default=None, null=True)
    client_uri_es_es = fields.CharField(max_length=255, description="Client URI (Spanish (Spain))",
                                        default=None, null=True)
    client_uri_es_gt = fields.CharField(max_length=255, description="Client URI (Spanish (Guatemala))",
                                        default=None, null=True)
    client_uri_es_hn = fields.CharField(max_length=255, description="Client URI (Spanish (Honduras))",
                                        default=None, null=True)
    client_uri_es_mx = fields.CharField(max_length=255, description="Client URI (Spanish (Mexico))",
                                        default=None, null=True)
    client_uri_es_ni = fields.CharField(max_length=255, description="Client URI (Spanish (Nicaragua))",
                                        default=None, null=True)
    client_uri_es_pa = fields.CharField(max_length=255, description="Client URI (Spanish (Panama))",
                                        default=None, null=True)
    client_uri_es_pe = fields.CharField(max_length=255, description="Client URI (Spanish (Peru))",
                                        default=None, null=True)
    client_uri_es_pr = fields.CharField(max_length=255, description="Client URI (Spanish (Puerto Rico))",
                                        default=None, null=True)
    client_uri_es_py = fields.CharField(max_length=255, description="Client URI (Spanish (Paraguay))",
                                        default=None, null=True)
    client_uri_es_sv = fields.CharField(max_length=255, description="Client URI (Spanish (El Salvador))",
                                        default=None, null=True)
    client_uri_es_uy = fields.CharField(max_length=255, description="Client URI (Spanish (Uruguay))",
                                        default=None, null=True)
    client_uri_es_ve = fields.CharField(max_length=255, description="Client URI (Spanish (Venezuela))",
                                        default=None, null=True)
    client_uri_et_ee = fields.CharField(max_length=255, description="Client URI (Estonian (Estonia))",
                                        default=None, null=True)
    client_uri_eu_es = fields.CharField(max_length=255, description="Client URI (Basque (Spain))",
                                        default=None, null=True)
    client_uri_fa_ir = fields.CharField(max_length=255, description="Client URI (Farsi (Iran))", default=None,
                                        null=True)
    client_uri_fi_fi = fields.CharField(max_length=255, description="Client URI (Finnish (Finland))",
                                        default=None, null=True)
    client_uri_fo_fo = fields.CharField(max_length=255, description="Client URI (Faroese (Faroe Islands))",
                                        default=None, null=True)
    client_uri_fr_be = fields.CharField(max_length=255, description="Client URI (French (Belgium))",
                                        default=None, null=True)
    client_uri_fr_ca = fields.CharField(max_length=255, description="Client URI (French (Canada))",
                                        default=None, null=True)
    client_uri_fr_ch = fields.CharField(max_length=255, description="Client URI (French (Switzerland))",
                                        default=None, null=True)
    client_uri_fr_fr = fields.CharField(max_length=255, description="Client URI (French (France))",
                                        default=None, null=True)
    client_uri_fr_lu = fields.CharField(max_length=255, description="Client URI (French (Luxembourg))",
                                        default=None, null=True)
    client_uri_fr_mc = fields.CharField(max_length=255,
                                        description="Client URI (French (Principality of Monaco))",
                                        default=None, null=True)
    client_uri_gl_es = fields.CharField(max_length=255, description="Client URI (Galician (Spain))",
                                        default=None, null=True)
    client_uri_gu_in = fields.CharField(max_length=255, description="Client URI (Gujarati (India))",
                                        default=None, null=True)
    client_uri_he_il = fields.CharField(max_length=255, description="Client URI (Hebrew (Israel))",
                                        default=None, null=True)
    client_uri_hi_in = fields.CharField(max_length=255, description="Client URI (Hindi (India))", default=None,
                                        null=True)
    client_uri_hr_ba = fields.CharField(max_length=255,
                                        description="Client URI (Croatian (Bosnia and Herzegovina))", default=None,
                                        null=True)
    client_uri_hr_hr = fields.CharField(max_length=255, description="Client URI (Croatian (Croatia))",
                                        default=None, null=True)
    client_uri_hu_hu = fields.CharField(max_length=255, description="Client URI (Hungarian (Hungary))",
                                        default=None, null=True)
    client_uri_hy_am = fields.CharField(max_length=255, description="Client URI (Armenian (Armenia))",
                                        default=None, null=True)
    client_uri_id_id = fields.CharField(max_length=255, description="Client URI (Indonesian (Indonesia))",
                                        default=None, null=True)
    client_uri_is_is = fields.CharField(max_length=255, description="Client URI (Icelandic (Iceland))",
                                        default=None, null=True)
    client_uri_it_ch = fields.CharField(max_length=255, description="Client URI (Italian (Switzerland))",
                                        default=None, null=True)
    client_uri_it_it = fields.CharField(max_length=255, description="Client URI (Italian (Italy))",
                                        default=None, null=True)
    client_uri_ja_jp = fields.CharField(max_length=255, description="Client URI (Japanese (Japan))",
                                        default=None, null=True)
    client_uri_ka_ge = fields.CharField(max_length=255, description="Client URI (Georgian (Georgia))",
                                        default=None, null=True)
    client_uri_kk_kz = fields.CharField(max_length=255, description="Client URI (Kazakh (Kazakhstan))",
                                        default=None, null=True)
    client_uri_kn_in = fields.CharField(max_length=255, description="Client URI (Kannada (India))",
                                        default=None, null=True)
    client_uri_ko_kr = fields.CharField(max_length=255, description="Client URI (Korean (Korea))",
                                        default=None, null=True)
    client_uri_kok_in = fields.CharField(max_length=255, description="Client URI (Konkani (India))",
                                         default=None, null=True)
    client_uri_ky_kg = fields.CharField(max_length=255, description="Client URI (Kyrgyz (Kyrgyzstan))",
                                        default=None, null=True)
    client_uri_lt_lt = fields.CharField(max_length=255, description="Client URI (Lithuanian (Lithuania))",
                                        default=None, null=True)
    client_uri_lv_lv = fields.CharField(max_length=255, description="Client URI (Latvian (Latvia))",
                                        default=None, null=True)
    client_uri_mi_nz = fields.CharField(max_length=255, description="Client URI (Maori (New Zealand))",
                                        default=None, null=True)
    client_uri_mk_mk = fields.CharField(max_length=255,
                                        description="Client URI (FYRO Macedonian (Former Yugoslav Republic of Macedonia))",
                                        default=None, null=True)
    client_uri_mn_mn = fields.CharField(max_length=255, description="Client URI (Mongolian (Mongolia))",
                                        default=None, null=True)
    client_uri_mr_in = fields.CharField(max_length=255, description="Client URI (Marathi (India))",
                                        default=None, null=True)
    client_uri_ms_bn = fields.CharField(max_length=255, description="Client URI (Malay (Brunei Darussalam))",
                                        default=None, null=True)
    client_uri_ms_my = fields.CharField(max_length=255, description="Client URI (Malay (Malaysia))",
                                        default=None, null=True)
    client_uri_mt_mt = fields.CharField(max_length=255, description="Client URI (Maltese (Malta))",
                                        default=None, null=True)
    client_uri_nb_no = fields.CharField(max_length=255, description="Client URI (Norwegian (Bokm?l) (Norway))",
                                        default=None, null=True)
    client_uri_nl_be = fields.CharField(max_length=255, description="Client URI (Dutch (Belgium))",
                                        default=None, null=True)
    client_uri_nl_nl = fields.CharField(max_length=255, description="Client URI (Dutch (Netherlands))",
                                        default=None, null=True)
    client_uri_nn_no = fields.CharField(max_length=255,
                                        description="Client URI (Norwegian (Nynorsk) (Norway))",
                                        default=None, null=True)
    client_uri_ns_za = fields.CharField(max_length=255,
                                        description="Client URI (Northern Sotho (South Africa))",
                                        default=None, null=True)
    client_uri_pa_in = fields.CharField(max_length=255, description="Client URI (Punjabi (India))",
                                        default=None, null=True)
    client_uri_pl_pl = fields.CharField(max_length=255, description="Client URI (Polish (Poland))",
                                        default=None, null=True)
    client_uri_ps_ar = fields.CharField(max_length=255, description="Client URI (Pashto (Afghanistan))",
                                        default=None, null=True)
    client_uri_pt_br = fields.CharField(max_length=255, description="Client URI (Portuguese (Brazil))",
                                        default=None, null=True)
    client_uri_pt_pt = fields.CharField(max_length=255, description="Client URI (Portuguese (Portugal))",
                                        default=None, null=True)
    client_uri_qu_bo = fields.CharField(max_length=255, description="Client URI (Quechua (Bolivia))",
                                        default=None, null=True)
    client_uri_qu_ec = fields.CharField(max_length=255, description="Client URI (Quechua (Ecuador))",
                                        default=None, null=True)
    client_uri_qu_pe = fields.CharField(max_length=255, description="Client URI (Quechua (Peru))",
                                        default=None, null=True)
    client_uri_ro_ro = fields.CharField(max_length=255, description="Client URI (Romanian (Romania))",
                                        default=None, null=True)
    client_uri_ru_ru = fields.CharField(max_length=255, description="Client URI (Russian (Russia))",
                                        default=None, null=True)
    client_uri_sa_in = fields.CharField(max_length=255, description="Client URI (Sanskrit (India))",
                                        default=None, null=True)
    client_uri_se_fi = fields.CharField(max_length=255, description="Client URI (Sami (Finland))",
                                        default=None, null=True)
    client_uri_se_no = fields.CharField(max_length=255, description="Client URI (Sami (Norway))", default=None,
                                        null=True)
    client_uri_se_se = fields.CharField(max_length=255, description="Client URI (Sami (Sweden))", default=None,
                                        null=True)
    client_uri_sk_sk = fields.CharField(max_length=255, description="Client URI (Slovak (Slovakia))",
                                        default=None, null=True)
    client_uri_sl_si = fields.CharField(max_length=255, description="Client URI (Slovenian (Slovenia))",
                                        default=None, null=True)
    client_uri_sq_al = fields.CharField(max_length=255, description="Client URI (Albanian (Albania))",
                                        default=None, null=True)
    client_uri_sr_ba = fields.CharField(max_length=255,
                                        description="Client URI (Serbian (Latin) (Bosnia and Herzegovina))",
                                        default=None, null=True)
    client_uri_sr_cyrl_ba = fields.CharField(max_length=255,
                                             description="Client URI (Serbian (Cyrillic) (Bosnia and Herzegovina))",
                                             default=None, null=True)
    client_uri_sr_sp = fields.CharField(max_length=255,
                                        description="Client URI (Serbian (Latin) (Serbia and Montenegro))",
                                        default=None, null=True)
    client_uri_sr_cyrl_sp = fields.CharField(max_length=255,
                                             description="Client URI (Serbian (Cyrillic) (Serbia and Montenegro))",
                                             default=None, null=True)
    client_uri_sv_fi = fields.CharField(max_length=255, description="Client URI (Swedish (Finland))",
                                        default=None, null=True)
    client_uri_sv_se = fields.CharField(max_length=255, description="Client URI (Swedish (Sweden))",
                                        default=None, null=True)
    client_uri_sw_ke = fields.CharField(max_length=255, description="Client URI (Swahili (Kenya))",
                                        default=None, null=True)
    client_uri_syr_sy = fields.CharField(max_length=255, description="Client URI (Syriac (Syria))",
                                         default=None, null=True)
    client_uri_ta_in = fields.CharField(max_length=255, description="Client URI (Tamil (India))", default=None,
                                        null=True)
    client_uri_te_in = fields.CharField(max_length=255, description="Client URI (Telugu (India))",
                                        default=None, null=True)
    client_uri_th_th = fields.CharField(max_length=255, description="Client URI (Thai (Thailand))",
                                        default=None, null=True)
    client_uri_tl_ph = fields.CharField(max_length=255, description="Client URI (Tagalog (Philippines))",
                                        default=None, null=True)
    client_uri_tn_za = fields.CharField(max_length=255, description="Client URI (Tswana (South Africa))",
                                        default=None, null=True)
    client_uri_tr_tr = fields.CharField(max_length=255, description="Client URI (Turkish (Turkey))",
                                        default=None, null=True)
    client_uri_tt_ru = fields.CharField(max_length=255, description="Client URI (Tatar (Russia))",
                                        default=None, null=True)
    client_uri_uk_ua = fields.CharField(max_length=255, description="Client URI (Ukrainian (Ukraine))",
                                        default=None, null=True)
    client_uri_ur_pk = fields.CharField(max_length=255,
                                        description="Client URI (Urdu (Islamic Republic of Pakistan))",
                                        default=None, null=True)
    client_uri_uz_uz = fields.CharField(max_length=255, description="Client URI (Uzbek (Latin) (Uzbekistan))",
                                        default=None, null=True)
    client_uri_uz_cyrl_uz = fields.CharField(max_length=255,
                                             description="Client URI (Uzbek (Cyrillic) (Uzbekistan))",
                                             default=None, null=True)
    client_uri_vi_vn = fields.CharField(max_length=255, description="Client URI (Vietnamese (Viet Nam))",
                                        default=None, null=True)
    client_uri_xh_za = fields.CharField(max_length=255, description="Client URI (Xhosa (South Africa))",
                                        default=None, null=True)
    client_uri_zh_cn = fields.CharField(max_length=255, description="Client URI (Chinese (S))", default=None,
                                        null=True)
    client_uri_zh_hk = fields.CharField(max_length=255, description="Client URI (Chinese (Hong Kong))",
                                        default=None, null=True)
    client_uri_zh_mo = fields.CharField(max_length=255, description="Client URI (Chinese (Macau))",
                                        default=None, null=True)
    client_uri_zh_sg = fields.CharField(max_length=255, description="Client URI (Chinese (Singapore))",
                                        default=None, null=True)
    client_uri_zh_tw = fields.CharField(max_length=255, description="Client URI (Chinese (T))", default=None,
                                        null=True)
    client_uri_zu_za = fields.CharField(max_length=255, description="Client URI (Zulu (South Africa))",
                                        default=None, null=True)
