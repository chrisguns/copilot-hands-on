/**
 * Validates a phone number.
 * @param {string} phoneNumber - The phone number to validate.
 * @returns {boolean} - True if the phone number is valid, false otherwise.
 */
function validatePhoneNumber(phoneNumber) {
    // Regular expression to validate global phone numbers
    const regex = /^\+(?:[0-9] ?){6,14}[0-9]$/;

    return regex.test(phoneNumber);
}
const stateAreaCodes = {
    "CA": ["213", "310", "323", "408", "415"],
    "NY": ["212", "315", "516", "518", "607"],
    "TX": ["210", "214", "254", "281", "325"],
    "FL": ["239", "305", "321", "352", "386"],
    "IL": ["217", "224", "309", "312", "331"],
    "GA": ["229", "404", "470", "478", "678"],
    "MI": ["231", "248", "269", "313", "517"],
    "NC": ["252", "336", "704", "828", "910"],
    "OH": ["216", "330", "419", "440", "513"],
    "PA": ["215", "267", "412", "484", "570"],
    "NJ": ["201", "551", "609", "732", "848"],
    "VA": ["276", "434", "540", "571", "703"],
    "WA": ["206", "253", "360", "425", "509"],
    "AZ": ["480", "520", "602", "623", "928"],
    "MA": ["339", "351", "413", "508", "617"],
    "IN": ["219", "260", "317", "574", "765"],
    "TN": ["423", "615", "731", "865", "901"],
    "MO": ["314", "417", "573", "636", "660"],
    "MD": ["240", "301", "410", "443", "667"],
    "WI": ["262", "414", "608", "715", "920"],
    "MN": ["218", "320", "507", "612", "651"],
    "CO": ["303", "719", "720", "970"],
    "AL": ["205", "251", "256", "334", "938"],
    "SC": ["803", "843", "864"],
    "LA": ["225", "318", "337", "504", "985"],
    "KY": ["270", "364", "502", "606", "859"],
    "OR": ["458", "503", "541", "971"],
    "OK": ["405", "539", "580", "918"],
    "CT": ["203", "475", "860", "959"],
    "IA": ["319", "515", "563", "641", "712"],
    "MS": ["228", "601", "662", "769"],
    "AR": ["479", "501", "870"],
    "UT": ["385", "435", "801"],
    "KS": ["316", "620", "785", "913"],
    "NV": ["702", "725", "775"],
};

// Usage
console.log(stateAreaCodes["CA"]);  // Output: ["213", "310", "323", "408", "415"]
