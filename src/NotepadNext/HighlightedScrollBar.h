/*
 * This file is part of Notepad Next.
 * Copyright 2019 Justin Dailey
 *
 * Notepad Next is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * Notepad Next is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with Notepad Next.  If not, see <https://www.gnu.org/licenses/>.
 */


#ifndef HIGHLIGHTEDSCROLLBAR_H
#define HIGHLIGHTEDSCROLLBAR_H

#include <QScrollBar>
#include <QPointer>

#include "ScintillaEdit.h"
#include "Plugin.h"


class HighlightedScrollBar;

class HighlightedScrollBarPlugin : public Plugin
{
    Q_OBJECT

public:
    HighlightedScrollBarPlugin(ScintillaEdit *editor);
    ~HighlightedScrollBarPlugin() override;

    struct Highlight {
        int line;
        Qt::GlobalColor color;
    };
    Highlight cursor;

public slots:
    void notify(const SCNotification *pscn) override;

private:
    HighlightedScrollBar *scrollBar = nullptr;
};


class HighlightedScrollBar : public QScrollBar
{
    Q_OBJECT

public:
    explicit HighlightedScrollBar(HighlightedScrollBarPlugin *plugin, Qt::Orientation orientation, QWidget *parent = nullptr)
        : QScrollBar(orientation, parent), plugin(plugin) {}

protected:
    void paintEvent(QPaintEvent *event) override;

private:
    void drawMarker(QPainter &p, int marker);
    void drawIndicator(QPainter &p, int indicator);

    HighlightedScrollBarPlugin *plugin;
};

#endif // HIGHLIGHTEDSCROLLBAR_H
