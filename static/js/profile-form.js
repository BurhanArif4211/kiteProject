

$(document).ready(function () {
  var $cat = $("select[name=country]"),
    $items = $("select[name=items]");

  $cat.change(function () {
    var $this = $(this).find(":selected"),
      rel = $this.attr("rel"),
      $set = $items.find("option." + rel);

    if ($set.size() < 0) {
      $items.hide();
      return;
    }

    $items.show().find("option").hide();

    $set.show().first().prop("selected", true);
  });

  //copy phone number to coupon

  $("#phone").change(function () {
    $("#coupon").val($(this).val());
  });

  //reset the forms

  resetForms();
  function resetForms() {
    for (i = 0; i < document.forms.length; i++) {
      document.forms[i].reset();
    }
  }
});

//Phone format

$.fn.ForceNumericOnly = function () {
  return this.each(function () {
    $(this).keydown(function (e) {
      var key = e.charCode || e.keyCode || 0;
      // allow backspace, tab, delete, enter, arrows, numbers and keypad numbers ONLY
      // home, end, period, and numpad decimal
      return (
        key == 8 || //backspace
        key == 9 || //tab
        key == 13 || //enter
        key == 46 || //delete
        key == 110 || //decimal point
        key == 190 || //period
        (key >= 35 && key <= 40) || //end,home,arrows,insert,delete
        (key >= 48 && key <= 57) || //numbers
        (key >= 96 && key <= 105)
      ); //numpad 0-9
    });
  });
};
$("#phone").ForceNumericOnly();

$("#btnContact").click(function (e) {
  var sCountry = $("#countries").val();
  var sPhone = $("#phone").val();

  if (
    sCountry == "Country" ||
    $("#pincode").val() == "Code" ||
    sPhone.length == 0
  ) {
    $(".error-message").show();
    $(".error-message").fadeOut(2000);
    $(".success-message").hide();
    e.preventDefault();
  } else if (sPhone.length <= 9) {
    $(".error-phone").show();
    $(".error-phone").fadeOut(2000);
    $(".success-message").hide();
    e.preventDefault();
  } else {
    $(".success-message").show();
    $(".error-message").hide();
    $(".success-message").fadeOut(5000);
  }
});

/*
Object of countries based on
http://en.wikipedia.org/wiki/List_of_IOC_country_codes
*/
function countriesDropdown(container) {
  var countries = {
    AFG: "Afghanistan",
    ALB: "Albania",
    ALG: "Algeria",
    AND: "Andorra",
    ANG: "Angola",
    ANT: "Antigua and Barbuda",
    ARG: "Argentina",
    ARM: "Armenia",
    ARU: "Aruba",
    ASA: "American Samoa",
    AUS: "Australia",
    AUT: "Austria",
    AZE: "Azerbaijan",
    BAH: "Bahamas",
    BAN: "Bangladesh",
    BAR: "Barbados",
    BDI: "Burundi",
    BEL: "Belgium",
    BEN: "Benin",
    BER: "Bermuda",
    BHU: "Bhutan",
    BIH: "Bosnia and Herzegovina",
    BIZ: "Belize",
    BLR: "Belarus",
    BOL: "Bolivia",
    BOT: "Botswana",
    BRA: "Brazil",
    BRN: "Bahrain",
    BRU: "Brunei",
    BUL: "Bulgaria",
    BUR: "Burkina Faso",
    CAF: "Central African Republic",
    CAM: "Cambodia",
    CAN: "Canada",
    CAY: "Cayman Islands",
    CGO: "Congo",
    CHA: "Chad",
    CHI: "Chile",
    CHN: "China",
    CIV: "Cote d'Ivoire",
    CMR: "Cameroon",
    COD: "DR Congo",
    COK: "Cook Islands",
    COL: "Colombia",
    COM: "Comoros",
    CPV: "Cape Verde",
    CRC: "Costa Rica",
    CRO: "Croatia",
    CUB: "Cuba",
    CYP: "Cyprus",
    CZE: "Czech Republic",
    DEN: "Denmark",
    DJI: "Djibouti",
    DMA: "Dominica",
    DOM: "Dominican Republic",
    ECU: "Ecuador",
    EGY: "Egypt",
    ERI: "Eritrea",
    ESA: "El Salvador",
    ESP: "Spain",
    EST: "Estonia",
    ETH: "Ethiopia",
    FIJ: "Fiji",
    FIN: "Finland",
    FRA: "France",
    FSM: "Micronesia",
    GAB: "Gabon",
    GAM: "Gambia",
    GBR: "Great Britain",
    GBS: "Guinea-Bissau",
    GEO: "Georgia",
    GEQ: "Equatorial Guinea",
    GER: "Germany",
    GHA: "Ghana",
    GRE: "Greece",
    GRN: "Grenada",
    GUA: "Guatemala",
    GUI: "Guinea",
    GUM: "Guam",
    GUY: "Guyana",
    HAI: "Haiti",
    HKG: "Hong Kong",
    HON: "Honduras",
    HUN: "Hungary",
    INA: "Indonesia",
    IND: "India",
    IRI: "Iran",
    IRL: "Ireland",
    IRQ: "Iraq",
    ISL: "Iceland",
    ISR: "Israel",
    ISV: "Virgin Islands",
    ITA: "Italy",
    IVB: "British Virgin Islands",
    JAM: "Jamaica",
    JOR: "Jordan",
    JPN: "Japan",
    KAZ: "Kazakhstan",
    KEN: "Kenya",
    KGZ: "Kyrgyzstan",
    KIR: "Kiribati",
    KOR: "South Korea",
    KOS: "Kosovo",
    KSA: "Saudi Arabia",
    KUW: "Kuwait",
    LAO: "Laos",
    LAT: "Latvia",
    LBA: "Libya",
    LBR: "Liberia",
    LCA: "Saint Lucia",
    LES: "Lesotho",
    LIB: "Lebanon",
    LIE: "Liechtenstein",
    LTU: "Lithuania",
    LUX: "Luxembourg",
    MAD: "Madagascar",
    MAR: "Morocco",
    MAS: "Malaysia",
    MAW: "Malawi",
    MDA: "Moldova",
    MDV: "Maldives",
    MEX: "Mexico",
    MGL: "Mongolia",
    MHL: "Marshall Islands",
    MKD: "Macedonia",
    MLI: "Mali",
    MLT: "Malta",
    MNE: "Montenegro",
    MON: "Monaco",
    MOZ: "Mozambique",
    MRI: "Mauritius",
    MTN: "Mauritania",
    MYA: "Myanmar",
    NAM: "Namibia",
    NCA: "Nicaragua",
    NED: "Netherlands",
    NEP: "Nepal",
    NGR: "Nigeria",
    NIG: "Niger",
    NOR: "Norway",
    NRU: "Nauru",
    NZL: "New Zealand",
    OMA: "Oman",
    PAK: "Pakistan",
    PAN: "Panama",
    PAR: "Paraguay",
    PER: "Peru",
    PHI: "Philippines",
    PLE: "Palestine",
    PLW: "Palau",
    PNG: "Papua New Guinea",
    POL: "Poland",
    POR: "Portugal",
    PRK: "North Korea",
    PUR: "Puerto Rico",
    QAT: "Qatar",
    ROU: "Romania",
    RSA: "South Africa",
    RUS: "Russia",
    RWA: "Rwanda",
    SAM: "Samoa",
    SEN: "Senegal",
    SEY: "Seychelles",
    SIN: "Singapore",
    SKN: "Saint Kitts and Nevis",
    SLE: "Sierra Leone",
    SLO: "Slovenia",
    SMR: "San Marino",
    SOL: "Solomon Islands",
    SOM: "Somalia",
    SRB: "Serbia",
    SRI: "Sri Lanka",
    SSD: "South Sudan",
    STP: "Sao Tome and Principe",
    SUD: "Sudan",
    SUI: "Switzerland",
    SUR: "Suriname",
    SVK: "Slovakia",
    SWE: "Sweden",
    SWZ: "Swaziland",
    SYR: "Syria",
    TAN: "Tanzania",
    TGA: "Tonga",
    THA: "Thailand",
    TJK: "Tajikistan",
    TKM: "Turkmenistan",
    TLS: "Timor-Leste",
    TOG: "Togo",
    TPE: "Chinese Taipei",
    TTO: "Trinidad and Tobago",
    TUN: "Tunisia",
    TUR: "Turkey",
    TUV: "Tuvalu",
    UAE: "United Arab Emirates",
    UGA: "Uganda",
    UKR: "Ukraine",
    URU: "Uruguay",
    USA: "United States",
    UZB: "Uzbekistan",
    VAN: "Vanuatu",
    VEN: "Venezuela",
    VIE: "Vietnam",
    VIN: "Saint Vincent and the Grenadines",
    YEM: "Yemen",
    ZAM: "Zambia",
    ZAN: "Zanzibar",
    ZIM: "Zimbabwe",
  };
  var out = "<select><option rel=''>Country</option>";
  for (var key in countries) {
    out += "<option rel='" + key + "'>" + countries[key] + "</option>";
  }
  out += "</select>";

  document.getElementById(container).innerHTML = out;
}
countriesDropdown("countries");



