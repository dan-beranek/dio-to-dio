-- Present Claude's Chapter 8 matrix as structured evidence records.
-- The original Markdown and PDF files remain untouched.

local field_labels = {
  "Observed condition",
  "DIO/ODI interpretation",
  "Task and observer affected",
  "Alternative pathway",
  "Significance for the whole"
}

function Table(tbl)
  if #tbl.head.rows == 0 then return nil end

  local header = tbl.head.rows[1]
  local labels = {}
  for i, cell in ipairs(header.cells) do
    labels[i] = pandoc.utils.stringify(cell.contents)
  end

  -- Target the Chapter 8 matrix by its exact first-column heading.
  if labels[1] ~= "Observed condition (a)" then return nil end
  if #labels ~= #field_labels then
    error("Claude Chapter 8 evidence matrix has an unexpected number of columns.")
  end

  local cards = pandoc.Blocks{}
  local observation_number = 0

  for _, body in ipairs(tbl.bodies) do
    for _, row in ipairs(body.body) do
      observation_number = observation_number + 1
      local card_blocks = pandoc.Blocks{}

      local card_header = pandoc.Div(
        pandoc.Blocks{
          pandoc.Para({
            pandoc.Str("Evidence item " .. string.format("%02d", observation_number))
          })
        },
        pandoc.Attr("", {"report-table-card-header"})
      )
      card_blocks:insert(card_header)

      local fields = pandoc.Blocks{}
      for i, cell in ipairs(row.cells) do
        local field_blocks = pandoc.Blocks{
          pandoc.Para({pandoc.Strong(field_labels[i])})
        }
        for _, block in ipairs(cell.contents) do
          field_blocks:insert(block)
        end

        local classes = {"report-table-card-field"}
        if i == 1 then
          table.insert(classes, "report-table-card-field-primary")
        end
        fields:insert(pandoc.Div(field_blocks, pandoc.Attr("", classes)))
      end

      card_blocks:insert(
        pandoc.Div(fields, pandoc.Attr("", {"report-table-card-fields"}))
      )
      cards:insert(pandoc.Div(card_blocks, pandoc.Attr("", {"report-table-card"})))
    end
  end

  return pandoc.Div(cards, pandoc.Attr("", {"report-table-cards"}))
end
