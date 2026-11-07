-- This filter changes only the HTML presentation of Claude's Chapter 8 matrix.
-- The original Markdown and PDF files remain untouched.

function Table(tbl)
  if #tbl.head.rows == 0 then return nil end

  local header = tbl.head.rows[1]
  local labels = {}
  for i, cell in ipairs(header.cells) do
    labels[i] = pandoc.utils.stringify(cell.contents)
  end

  -- Target the Chapter 8 matrix by its exact first-column heading.
  if labels[1] ~= "Observed condition (a)" then return nil end

  local cards = pandoc.Blocks{}
  for _, body in ipairs(tbl.bodies) do
    for _, row in ipairs(body.body) do
      local card_blocks = pandoc.Blocks{}
      local title_blocks = pandoc.Blocks{
        pandoc.Para({pandoc.Strong(labels[1])})
      }
      for _, block in ipairs(row.cells[1].contents) do
        title_blocks:insert(block)
      end
      card_blocks:insert(pandoc.Div(title_blocks, pandoc.Attr("", {"report-table-card-title"})))

      for i = 2, #row.cells do
        local field_blocks = pandoc.Blocks{
          pandoc.Para({pandoc.Strong(labels[i])})
        }
        for _, block in ipairs(row.cells[i].contents) do
          field_blocks:insert(block)
        end
        card_blocks:insert(pandoc.Div(field_blocks, pandoc.Attr("", {"report-table-card-field"})))
      end

      cards:insert(pandoc.Div(card_blocks, pandoc.Attr("", {"report-table-card"})))
    end
  end

  return pandoc.Div(cards, pandoc.Attr("", {"report-table-cards"}))
end
