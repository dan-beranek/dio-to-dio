local function trim(s)
  return (s:gsub("^%s+", ""):gsub("%s+$", ""))
end
local function html_escape(s)
  return s:gsub("&", "&amp;"):gsub("<", "&lt;"):gsub(">", "&gt;"):gsub('"', "&quot;")
end

function RawBlock(el)
  if el.format ~= "tex" then return nil end
  local s = el.text
  if s:match("\\begin{center}") and s:match("\\end{center}") then
    local title = s:match("{\\LARGE%s*(.-)\\par}") or s:match("{\\Large%s*(.-)\\par}")
    local byline = s:match("{\\large\\itshape%s*(.-)\\par}")
    local author = s:match("{\\large%s+(.-)\\par}")
    local rest = s
    rest = rest:gsub("\\begin{center}", ""):gsub("\\end{center}", "")
    rest = rest:gsub("{\\LARGE%s*.-\\par}", ""):gsub("{\\Large%s*.-\\par}", "")
    rest = rest:gsub("{\\large\\itshape%s*.-\\par}", ""):gsub("{\\large%s*.-\\par}", "")
    rest = rest:gsub("\\vspace%b{}", ""):gsub("\\par", "\n")
    local details = {}
    for line in rest:gmatch("[^\r\n]+") do
      line = trim(line:gsub("[{}]", ""))
      if line ~= "" then table.insert(details, line) end
    end
    local parts = { '<header class="source-title-block">' }
    if title then table.insert(parts, '<div class="source-title">' .. html_escape(trim(title)) .. '</div>') end
    if byline then table.insert(parts, '<div class="source-byline"><em>' .. html_escape(trim(byline)) .. '</em></div>') end
    if author then table.insert(parts, '<div class="source-author">' .. html_escape(trim(author)) .. '</div>') end
    for _, line in ipairs(details) do
      table.insert(parts, '<div class="source-title-detail">' .. html_escape(line) .. '</div>')
    end
    table.insert(parts, '</header>')
    return pandoc.RawBlock("html", table.concat(parts, "\n"))
  end
  -- A page break is a print-layout instruction, not report prose.
  if trim(s) == "\\newpage" then return {} end
  -- Never discard an unrecognized TeX block; expose its source verbatim.
  return pandoc.CodeBlock(s, pandoc.Attr("", {"raw-tex-source"}))
end

function RawInline(el)
  -- A literal HTML tag used as an example must remain visible as text.
  if el.format == "html" and el.text:match("^<link%s") then
    return pandoc.Str(el.text)
  end
  return nil
end
