import { OnInit } from '@angular/core';
import { Component } from '@angular/core';
import { LayoutService } from './service/app.layout.service';

@Component({
  selector: 'app-menu',
  templateUrl: './app.menu.component.html'
})
export class AppMenuComponent implements OnInit {

  model: any[] = [];
  constructor(public layoutService: LayoutService) { }

  ngOnInit() {

    this.model = [
      {
        label: 'Users',
        items: [
          {
            label: 'User', icon: 'pi pi-id-card',
            routerLink: ['/admin/user'],
          },
          {
            label: 'Role', icon: 'pi pi-sitemap',
            routerLink: ['/admin/role'],
          },
          {
            label: 'Class', icon: 'pi pi-chart-bar',
            routerLink: ['/admin/class'],
          },
            {
                label: 'Attendance', icon: 'pi pi-share-alt',
                routerLink: ['/admin/attendance'],
            },

            {
                label: 'Announcement', icon: 'pi pi-tablet',
                routerLink: ['/admin/announcement'],
            },
        ]
      },
      {
        label: 'Account',
        items: [
          {
            label: 'Logout', icon: 'pi pi-sign-out',
            routerLink: ['/auth/login']
          }
        ]
      }
    ];
  }
}
