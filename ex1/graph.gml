graph [
  directed 1
  node [
    id 0
    label "B"
    labels 4
  ]
  node [
    id 1
    label "STR"
  ]
  node [
    id 2
    label "D"
    labels 3
  ]
  node [
    id 3
    label "E"
    labels 2
  ]
  node [
    id 4
    label "A"
    labels 1
  ]
  node [
    id 5
    label "F"
    labels 1
  ]
  node [
    id 6
    label "C"
    labels 2
  ]
  edge [
    source 0
    target 2
      weight "1"
      weight "2"
      weight "5"
  ]
  edge [
    source 1
    target 0
      weight "1"
      weight "2"
      weight "4"
      weight "5"
  ]
  edge [
    source 1
    target 4
      weight "3"
  ]
  edge [
    source 1
    target 6
      weight "6"
  ]
  edge [
    source 2
    target 3
      weight "2"
  ]
  edge [
    source 2
    target 6
      weight "5"
  ]
  edge [
    source 4
    target 5
      weight "3"
  ]
  edge [
    source 6
    target 3
      weight "6"
  ]
]
