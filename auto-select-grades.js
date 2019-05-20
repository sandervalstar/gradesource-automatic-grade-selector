var grades = {
    "StudentID1": "A",
    "StudentID2": "B"
};

var gradeSelectMap = {
    'A+': 427102,
    'A': 427101,
    'A-': 427100,
    'B+': 427099,
    'B': 427098,
    'B-': 427097,
    'C+': 427096,
    'C': 427095,
    'C-': 427094,
    'D+': 427093,
    'D': 427092,
    'D-': 427091,
    'F': 427090
};

for (var student in grades) {
    var xpath = "//tr[contains(., '" + student + "')]";
    var matchingElements = document.evaluate(xpath, document, null, XPathResult.ANY_TYPE, null);
    var studentRow = matchingElements.iterateNext();
    studentRow = matchingElements.iterateNext();
    studentRow = matchingElements.iterateNext();
    studentRow = matchingElements.iterateNext();
    
    if (studentRow) {
        var studentGradeSelector = studentRow.lastElementChild.firstElementChild;
        var studentGrade = grades[student];
        studentGradeSelector.value = gradeSelectMap[studentGrade];
    } else {
        console.warn("Couldn't find row for student:", student)
    }
}
